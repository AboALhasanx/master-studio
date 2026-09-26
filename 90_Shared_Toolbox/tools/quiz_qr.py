#!/usr/bin/env python3
"""
Master Studio LAN QR Code Generator Helper
------------------------------------------
Generates LAN-accessible quiz links and renders ASCII QR codes in the terminal
so mobile devices on the same Wi-Fi network can scan and take quizzes.
"""

import socket
import sys
from typing import Tuple


def get_lan_ip() -> str:
    """
    Detects host Wi-Fi / Ethernet LAN IPv4 address.
    Falls back to '127.0.0.1' if detection fails or network is unreachable.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Connecting to an address determines the default outbound interface IP
            s.connect(("10.255.255.255", 1))
            ip = s.getsockname()[0]
        except Exception:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        # If the detected IP is on a 10.x virtual/WireGuard range, check if a 192.168.x.x Wi-Fi NIC exists
        if ip.startswith("10."):
            try:
                hostname = socket.gethostname()
                ip_list = socket.gethostbyname_ex(hostname)[2]
                wifi_ips = [candidate for candidate in ip_list if candidate.startswith("192.168.")]
                if wifi_ips:
                    return wifi_ips[0]
            except Exception:
                pass

        return ip
    except Exception:
        return "127.0.0.1"


def check_adb_usb_device() -> bool:
    """
    Checks if an Android device is connected via USB/ADB.
    If connected, runs 'adb reverse tcp:5000 tcp:5000' so the phone
    can connect directly to http://localhost:5000 with zero Wi-Fi latency.
    """
    import subprocess
    try:
        res = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=2)
        lines = [line.strip() for line in res.stdout.strip().splitlines() if line.strip()]
        devices = [l for l in lines[1:] if "\tdevice" in l or " device" in l]
        if devices:
            subprocess.run(["adb", "reverse", "tcp:5000", "tcp:5000"], capture_output=True, timeout=2)
            return True
    except Exception:
        pass
    return False


def resolve_quiz_slug(subject_id: str, quiz_slug: str) -> str:
    """
    Resolves a short or case-insensitive quiz slug (e.g. 'Quiz_01')
    to the canonical filename stem (e.g. 'Quiz_01_Software_Crisis').
    """
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent.parent.parent
    clean_slug = quiz_slug.replace(".json", "").strip()
    semesters = sorted([d for d in base_dir.glob("0*_Semester_*") if d.is_dir()])

    for sem in semesters:
        quiz_dir = sem / subject_id / "07_Quizzes_&_Anki"
        if not quiz_dir.is_dir():
            for sdir in sem.iterdir():
                if sdir.is_dir() and subject_id.lower() in sdir.name.lower():
                    quiz_dir = sdir / "07_Quizzes_&_Anki"
                    break
        if quiz_dir.is_dir():
            files = list(quiz_dir.glob("Quiz_*.json"))
            for f in files:
                if f.stem.lower() == clean_slug.lower():
                    return f.stem
            for f in files:
                if f.stem.lower().startswith(clean_slug.lower()):
                    return f.stem
            for f in files:
                if clean_slug.lower() in f.stem.lower():
                    return f.stem
    return clean_slug

def generate_quiz_link(subject_id: str, quiz_id: str, print_qr: bool = True) -> Tuple[str, str]:
    """
    Generates the LAN URL for a quiz and optionally prints a clean terminal banner with ASCII QR code.

    Returns:
        (link, lan_ip):
            link: "http://{lan_ip}:5000/quiz/{subject_id}/{quiz_id}"
            lan_ip: detected host IP
    """
    canonical_quiz_id = resolve_quiz_slug(subject_id, quiz_id)
    lan_ip = get_lan_ip()
    link = f"http://{lan_ip}:5000/quiz/{subject_id}/{canonical_quiz_id}"
    local_link = f"http://localhost:5000/quiz/{subject_id}/{canonical_quiz_id}"
    usb_active = check_adb_usb_device()
    if print_qr:
        print("=" * 60)
        print("📱 MASTER STUDIO INTERACTIVE QUIZ PORTAL")
        print("=" * 60)
        print(f"🔗 LAN URL (Mobile/Tablet): {link}")
        print(f"💻 Local URL (Browser)   : {local_link}")
        if usb_active:
            print("⚡ USB Cable Connected    : Active (adb reverse port 5000 forwarded)")
            print(f"📱 1-Tap USB Phone URL   : {local_link}")
        print("-" * 60)
        print("📲 Scan QR Code on your mobile device (same Wi-Fi):")
        print()

        try:
            import qrcode
            qr = qrcode.QRCode(border=1)
            qr.add_data(link)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
        except ImportError as e:
            import sys as _sys
            print("⚠️  Package 'qrcode' is not installed.")
            print(f"   ({e} — interpreter: {_sys.executable})")
            print("   To enable terminal QR codes, run: pip install qrcode")
        except Exception as e:
            print(f"⚠️  Could not render QR code ({e}). Open the link directly:")
            print(f"   {link}")

        print("=" * 60)

    return link, lan_ip


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate LAN QR Code for Master Studio Quiz")
    parser.add_argument("subject_id", help="Subject identifier (e.g. EE-201, MATH-101)")
    parser.add_argument("quiz_id", help="Quiz identifier (e.g. quiz-01, ch3-quiz)")
    parser.add_argument("--no-qr", action="store_true", help="Suppress QR code output")
    parser.add_argument("--open", "--browser", action="store_true", help="Open quiz directly in default browser (Chromium/Chrome)")
    parser.add_argument("--window", action="store_true", help="Launch in a standalone external CMD window on Windows")

    args = parser.parse_args()

    if args.open:
        import webbrowser
        link, lan_ip = generate_quiz_link(args.subject_id, args.quiz_id, print_qr=not args.no_qr)
        webbrowser.open(link)
        print(f"🌐 Opened quiz directly in default browser: {link}")
    elif args.window and sys.platform == "win32":
        import os
        from pathlib import Path
        script_path = Path(__file__).resolve()
        # Pin the child window to THIS interpreter (sys.executable) and UTF-8
        # output: a bare `python` in the spawned cmd can resolve to a different
        # install (e.g. the Windows Python Manager shim defaulting to 3.14)
        # that lacks the qrcode package or crashes on emoji output.
        cmd = (
            f'start "Master Studio Quiz Portal - {args.subject_id}" '
            f'cmd /k "{sys.executable} -X utf8 '
            f'\"{script_path}\" \"{args.subject_id}\" \"{args.quiz_id}\""'
        )
        os.system(cmd)
        print(f"🚀 Launched standalone QR window for {args.subject_id} / {args.quiz_id}")
    else:
        generate_quiz_link(args.subject_id, args.quiz_id, print_qr=not args.no_qr)
