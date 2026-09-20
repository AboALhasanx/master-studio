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
        return ip
    except Exception:
        return "127.0.0.1"


def generate_quiz_link(subject_id: str, quiz_id: str, print_qr: bool = True) -> Tuple[str, str]:
    """
    Generates the LAN URL for a quiz and optionally prints a clean terminal banner with ASCII QR code.

    Returns:
        (link, lan_ip):
            link: "http://{lan_ip}:5000/quiz/{subject_id}/{quiz_id}"
            lan_ip: detected host IP
    """
    lan_ip = get_lan_ip()
    link = f"http://{lan_ip}:5000/quiz/{subject_id}/{quiz_id}"
    local_link = f"http://localhost:5000/quiz/{subject_id}/{quiz_id}"

    if print_qr:
        print("=" * 60)
        print("📱 MASTER STUDIO INTERACTIVE QUIZ PORTAL")
        print("=" * 60)
        print(f"🔗 LAN URL (Mobile/Tablet): {link}")
        print(f"💻 Local URL (Browser)   : {local_link}")
        print("-" * 60)
        print("📲 Scan QR Code on your mobile device (same Wi-Fi):")
        print()

        try:
            import qrcode
            qr = qrcode.QRCode(border=1)
            qr.add_data(link)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
        except ImportError:
            print("⚠️  Package 'qrcode' is not installed.")
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
    parser.add_argument("--window", action="store_true", help="Launch in a standalone external CMD window on Windows")

    args = parser.parse_args()

    if args.window and sys.platform == "win32":
        import os
        from pathlib import Path
        script_path = Path(__file__).resolve()
        cmd = f'start "Master Studio Quiz Portal - {args.subject_id}" cmd /k "python \"{script_path}\" \"{args.subject_id}\" \"{args.quiz_id}\""'
        os.system(cmd)
        print(f"🚀 Launched standalone QR window for {args.subject_id} / {args.quiz_id}")
    else:
        generate_quiz_link(args.subject_id, args.quiz_id, print_qr=not args.no_qr)
