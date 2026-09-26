#!/usr/bin/env python3
"""
Master Studio Native APK Builder & Signer
-----------------------------------------
Compiles and signs the standalone Android APK (MSCQuiz_Signed.apk)
with full offline PWA bundling, Telegram JSON direct-open file handling,
Android Share Target support, and LAN PC synchronization.

Usage:
  python build_mscquiz_apk.py
"""

import os
import sys
import shutil
import subprocess
import zipfile
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SDK_ROOT = Path("C:/Android")
BUILD_TOOLS_DIR = SDK_ROOT / "build-tools" / "35.0.0"
PLATFORM_JAR = SDK_ROOT / "platforms" / "android-34" / "android.jar"
BUILD_DIR = REPO_ROOT / "91_Dashboard" / "android_build"
OUTPUT_APK = REPO_ROOT / "91_Dashboard" / "MSCQuiz_Signed.apk"
KEYSTORE_PATH = REPO_ROOT / "91_Dashboard" / "mscquiz-release.keystore"
KEYSTORE_PASS = "masterstudiopass"
KEY_ALIAS = "mscquiz"


def run_cmd(cmd_list, desc, check=True):
    print(f"  ▶ {desc}...")
    res = subprocess.run(cmd_list, capture_output=True, text=True, shell=True)
    if res.returncode != 0 and check:
        print(f"❌ Error during {desc}:", file=sys.stderr)
        print("STDOUT:\n", res.stdout, file=sys.stderr)
        print("STDERR:\n", res.stderr, file=sys.stderr)
        sys.exit(res.returncode)
    return res


def setup_project_tree():
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    src_dir = BUILD_DIR / "src" / "com" / "masterstudio" / "mscquiz"
    res_dir = BUILD_DIR / "res"
    values_dir = res_dir / "values"
    mipmap_hdpi = res_dir / "mipmap-hdpi"
    mipmap_xxhdpi = res_dir / "mipmap-xxhdpi"
    xml_dir = res_dir / "xml"
    assets_dir = BUILD_DIR / "assets"

    src_dir.mkdir(parents=True, exist_ok=True)
    values_dir.mkdir(parents=True, exist_ok=True)
    mipmap_hdpi.mkdir(parents=True, exist_ok=True)
    mipmap_xxhdpi.mkdir(parents=True, exist_ok=True)
    xml_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 1. Icons
    static_dir = REPO_ROOT / "91_Dashboard" / "static"
    shutil.copy2(static_dir / "icon-192.png", mipmap_hdpi / "ic_launcher.png")
    shutil.copy2(static_dir / "icon-512.png", mipmap_xxhdpi / "ic_launcher.png")

    # 2. strings.xml
    (values_dir / "strings.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">MSCQuiz</string>
</resources>
""", encoding="utf-8")

    # 3. file_paths.xml
    (xml_dir / "file_paths.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<paths>
    <external-path name="external_files" path="." />
    <cache-path name="cache_files" path="." />
</paths>
""", encoding="utf-8")

    # 4. Copy web assets to assets/ for 100% offline zero-server boot
    assets_static = assets_dir / "static"
    assets_static.mkdir(parents=True, exist_ok=True)
    
    # Copy template as index.html
    html_src = REPO_ROOT / "91_Dashboard" / "templates" / "quiz.html"
    html_content = html_src.read_text(encoding="utf-8")
    
    # Clean Jinja2 template tags for standalone asset rendering
    cleaned_html = html_content.replace("{% if page == 'history' %}سجل الاختبارات{% else %}الأسئلة المحفوظة{% endif %}", "MSCQuiz")
    cleaned_html = cleaned_html.replace("{{ lan_ip or '127.0.0.1' }}", "127.0.0.1")
    # Replace root element dynamic attributes
    cleaned_html = cleaned_html.replace('data-direct-mode="{% if direct_mode %}true{% else %}false{% endif %}"', 'data-direct-mode="false"')
    cleaned_html = cleaned_html.replace('data-subject-id="{{ subject_id or \'\' }}"', 'data-subject-id=""')
    cleaned_html = cleaned_html.replace('data-quiz-id="{{ quiz_id or \'\' }}"', 'data-quiz-id=""')
    cleaned_html = cleaned_html.replace('data-lan-ip="{{ lan_ip or \'127.0.0.1\' }}"', 'data-lan-ip="127.0.0.1"')
    
    # Remove Jinja loops
    import re
    cleaned_html = re.sub(r'\{% if not direct_mode and available_quizzes %\}.*?\{% endif %\}', '', cleaned_html, flags=re.DOTALL)
    cleaned_html = re.sub(r'\{% if shared_quizzes %\}.*?\{% endif %\}', '', cleaned_html, flags=re.DOTALL)
    cleaned_html = re.sub(r'\{%.*?%\}', '', cleaned_html)
    cleaned_html = re.sub(r'\{\{.*?\}\}', '', cleaned_html)
    # Fix paths from /static/ to static/
    cleaned_html = cleaned_html.replace('href="/static/', 'href="static/')
    cleaned_html = cleaned_html.replace('src="/static/', 'src="static/')

    (assets_dir / "index.html").write_text(cleaned_html, encoding="utf-8")

    # Copy static assets
    for item in static_dir.glob("*"):
        if item.is_file():
            shutil.copy2(item, assets_static / item.name)
        elif item.is_dir() and item.name == "sounds":
            shutil.copytree(item, assets_static / "sounds", dirs_exist_ok=True)

    # Copy bundled curriculum JSON into assets/ for instant 0ms seed
    hub_bundle = REPO_ROOT / "00_STUDIO_HUB" / "curriculum_quiz_bundle_sem1.json"
    if hub_bundle.is_file():
        shutil.copy2(hub_bundle, assets_dir / "curriculum_quiz_bundle_sem1.json")

    # 5. AndroidManifest.xml
    manifest_xml = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.masterstudio.mscquiz"
    android:versionCode="1"
    android:versionName="1.0.0">

    <uses-sdk android:minSdkVersion="24" android:targetSdkVersion="34" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />

    <application
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher"
        android:theme="@android:style/Theme.NoTitleBar"
        android:usesCleartextTraffic="true"
        android:allowBackup="true"
        android:supportsRtl="true">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTask"
            android:configChanges="orientation|screenSize|keyboardHidden|screenLayout">

            <!-- Main Launcher Intent -->
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

            <!-- Telegram & File Manager Direct Open (.json / .msquiz) -->
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="file" />
                <data android:scheme="content" />
                <data android:mimeType="application/json" />
                <data android:mimeType="text/plain" />
                <data android:mimeType="*/*" android:pathPattern=".*\\.json" />
                <data android:mimeType="*/*" android:pathPattern=".*\\.msquiz" />
            </intent-filter>

            <!-- Android Native Share Sheet Target (Telegram / WhatsApp Share) -->
            <intent-filter>
                <action android:name="android.intent.action.SEND" />
                <action android:name="android.intent.action.SEND_MULTIPLE" />
                <category android:name="android.intent.category.DEFAULT" />
                <data android:mimeType="application/json" />
                <data android:mimeType="text/plain" />
                <data android:mimeType="*/*" />
            </intent-filter>

        </activity>

    </application>
</manifest>
"""
    (BUILD_DIR / "AndroidManifest.xml").write_text(manifest_xml, encoding="utf-8")

    # 6. MainActivity.java
    main_activity_java = """package com.masterstudio.mscquiz;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Base64;
import android.webkit.ConsoleMessage;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

public class MainActivity extends Activity {
    private WebView webView;
    private ValueCallback<Uri[]> fileUploadCallback;
    private static final int FILE_CHOOSER_REQ = 1001;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setAllowFileAccessFromFileURLs(true);
        settings.setAllowUniversalAccessFromFileURLs(true);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);

        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onShowFileChooser(WebView wv, ValueCallback<Uri[]> filePathCallback, FileChooserParams fileChooserParams) {
                if (fileUploadCallback != null) {
                    fileUploadCallback.onReceiveValue(null);
                }
                fileUploadCallback = filePathCallback;

                Intent intent = fileChooserParams.createIntent();
                try {
                    startActivityForResult(intent, FILE_CHOOSER_REQ);
                } catch (Exception e) {
                    fileUploadCallback = null;
                    return false;
                }
                return true;
            }

            @Override
            public boolean onConsoleMessage(ConsoleMessage cm) {
                return super.onConsoleMessage(cm);
            }
        });

        webView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);
                handleIncomingIntent(getIntent());
            }
        });

        // Load self-contained offline asset package
        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        handleIncomingIntent(intent);
    }

    private void handleIncomingIntent(Intent intent) {
        if (intent == null) return;
        String action = intent.getAction();

        if (Intent.ACTION_VIEW.equals(action)) {
            Uri uri = intent.getData();
            if (uri != null) {
                importFromUri(uri);
            }
        } else if (Intent.ACTION_SEND.equals(action)) {
            Uri uri = intent.getParcelableExtra(Intent.EXTRA_STREAM);
            if (uri != null) {
                importFromUri(uri);
            }
        } else if (Intent.ACTION_SEND_MULTIPLE.equals(action)) {
            ArrayList<Uri> uris = intent.getParcelableArrayListExtra(Intent.EXTRA_STREAM);
            if (uris != null) {
                for (Uri uri : uris) {
                    importFromUri(uri);
                }
            }
        }
    }

    private void importFromUri(Uri uri) {
        try {
            InputStream is = getContentResolver().openInputStream(uri);
            if (is == null) return;
            BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line).append('\\n');
            }
            is.close();

            String jsonText = sb.toString();
            // Encode as Base64 to safely pass through evaluateJavascript
            String base64 = Base64.encodeToString(jsonText.getBytes(StandardCharsets.UTF_8), Base64.NO_WRAP);
            String js = "try { " +
                    "  const rawText = decodeURIComponent(escape(atob('" + base64 + "'))); " +
                    "  const data = JSON.parse(rawText); " +
                    "  if (window.quizApp && window.quizApp.processImportedQuizData) { " +
                    "    window.quizApp.processImportedQuizData(data, 'Telegram_Quiz').then(quizzes => { " +
                    "      if (quizzes && quizzes.length) { " +
                    "        window.quizApp.injectImportedQuizzesToCatalog(quizzes); " +
                    "        window.quizApp.showTemporaryToast('تم فتح وحفظ الكويز من تليغرام بنجاح!'); " +
                    "        if (quizzes.length === 1) { " +
                    "          window.quizApp.quizData = quizzes[0]; " +
                    "          window.quizApp.subjectId = quizzes[0].subject_id; " +
                    "          window.quizApp.quizId = quizzes[0].quiz_id; " +
                    "          window.quizApp.setupQuizSession(); " +
                    "        } " +
                    "      } " +
                    "    }); " +
                    "  } " +
                    "} catch (e) { console.error('Intent import error:', e); }";

            webView.post(() -> webView.evaluateJavascript(js, null));
        } catch (Exception e) {
            Toast.makeText(this, "خطأ في قراءة ملف الكويز: " + e.getMessage(), Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == FILE_CHOOSER_REQ) {
            if (fileUploadCallback == null) return;
            Uri[] results = null;
            if (resultCode == Activity.RESULT_OK && data != null) {
                String dataString = data.getDataString();
                if (dataString != null) {
                    results = new Uri[]{Uri.parse(dataString)};
                } else if (data.getClipData() != null) {
                    int count = data.getClipData().getItemCount();
                    results = new Uri[count];
                    for (int i = 0; i < count; i++) {
                        results[i] = data.getClipData().getItemAt(i).getUri();
                    }
                }
            }
            fileUploadCallback.onReceiveValue(results);
            fileUploadCallback = null;
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }

    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
"""
    (src_dir / "MainActivity.java").write_text(main_activity_java, encoding="utf-8")
    print("✅ Project tree and source files configured successfully.")


def ensure_keystore():
    if not KEYSTORE_PATH.exists():
        print("🔑 Generating release keystore for personal/development use...")
        keytool_cmd = (
            f'keytool -genkeypair -v -keystore "{KEYSTORE_PATH}" '
            f'-alias {KEY_ALIAS} -keyalg RSA -keysize 2048 -validity 10000 '
            f'-storepass {KEYSTORE_PASS} -keypass {KEYSTORE_PASS} '
            f'-dname "CN=MasterStudio, OU=MCS, O=UniversityOfWasit, L=Wasit, ST=Wasit, C=IQ"'
        )
        run_cmd(keytool_cmd, "Generate Keystore")
        print(f"✅ Keystore created: {KEYSTORE_PATH.name}")


def build_and_sign_apk():
    aapt2 = BUILD_TOOLS_DIR / "aapt2.exe"
    zipalign = BUILD_TOOLS_DIR / "zipalign.exe"
    d8 = BUILD_TOOLS_DIR / "d8.bat"
    apksigner = BUILD_TOOLS_DIR / "apksigner.bat"

    bin_dir = BUILD_DIR / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)

    # 1. Compile Resources
    res_zip = bin_dir / "compiled_res.zip"
    run_cmd(f'"{aapt2}" compile --dir "{BUILD_DIR}/res" -o "{res_zip}"', "AAPT2 Compile Resources")

    # 2. Link Resources & Generate R.java & unaligned APK
    unaligned_apk = bin_dir / "unaligned.apk"
    gen_dir = BUILD_DIR / "gen"
    gen_dir.mkdir(parents=True, exist_ok=True)
    
    run_cmd(
        f'"{aapt2}" link -I "{PLATFORM_JAR}" '
        f'--manifest "{BUILD_DIR}/AndroidManifest.xml" '
        f'-A "{BUILD_DIR}/assets" '
        f'-o "{unaligned_apk}" '
        f'--java "{gen_dir}" '
        f'"{res_zip}"',
        "AAPT2 Link Resources & Assets"
    )

    # 3. Compile Java with javac
    r_java = list(gen_dir.rglob("R.java"))[0]
    main_java = BUILD_DIR / "src" / "com" / "masterstudio" / "mscquiz" / "MainActivity.java"
    classes_dir = bin_dir / "classes"
    classes_dir.mkdir(parents=True, exist_ok=True)

    javac_cmd = f'javac -source 17 -target 17 -cp "{PLATFORM_JAR}" -d "{classes_dir}" "{r_java}" "{main_java}"'
    run_cmd(javac_cmd, "Compile Java Source (javac)")

    # 4. Compile Classes to DEX with D8
    class_files = [f'"{str(p)}"' for p in classes_dir.rglob("*.class")]
    run_cmd(
        f'cmd.exe /c "\"{d8}\" --min-api 24 --output \"{bin_dir}\" {" ".join(class_files)}"',
        "Compile Classes to DEX (D8)"
    )

    # 5. Insert classes.dex into unaligned APK
    dex_file = bin_dir / "classes.dex"
    with zipfile.ZipFile(unaligned_apk, "a") as z:
        z.write(dex_file, "classes.dex")
    print("  ▶ Injected classes.dex into APK.")

    # 6. Zipalign APK (4-byte boundary)
    aligned_apk = bin_dir / "aligned.apk"
    run_cmd(f'"{zipalign}" -f 4 "{unaligned_apk}" "{aligned_apk}"', "Zipalign APK")

    # 7. Sign APK with apksigner
    ensure_keystore()
    run_cmd(
        f'cmd.exe /c "\"{apksigner}\" sign --ks \"{KEYSTORE_PATH}\" --ks-key-alias {KEY_ALIAS} '
        f'--ks-pass pass:{KEYSTORE_PASS} --out \"{OUTPUT_APK}\" \"{aligned_apk}\""',
        "Sign APK with apksigner (v2/v3 signature scheme)"
    )

    # 8. Verify APK Signature
    ver_res = run_cmd(
        f'cmd.exe /c "\"{apksigner}\" verify --verbose \"{OUTPUT_APK}\""',
        "Verify APK Signature"
    )
    print("  ▶ Verification Output:", [line for line in ver_res.stdout.splitlines() if "Verified" in line or "Number of signers" in line])


def main():
    print("=================================================================")
    print("🚀 MASTER STUDIO NATIVE APK BUILDER & SIGNER: MSCQuiz")
    print("=================================================================")
    setup_project_tree()
    build_and_sign_apk()
    print("=================================================================")
    print(f"🎉 SUCCESS! Signed APK created successfully:")
    print(f"   Path: {OUTPUT_APK}")
    print(f"   Size: {OUTPUT_APK.stat().st_size / 1024:.1f} KB")
    print("=================================================================")


if __name__ == "__main__":
    main()
