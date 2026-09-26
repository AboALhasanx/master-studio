import sys
import json
import socket
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch, MagicMock
import pytest

# Add dashboard to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
dashboard_path = BASE_DIR / "91_Dashboard"
if str(dashboard_path) not in sys.path:
    sys.path.insert(0, str(dashboard_path))

import app as dashboard_app
from app import app, get_lan_ip


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_get_lan_ip_success():
    with patch("socket.socket") as mock_socket_cls:
        mock_sock = MagicMock()
        mock_sock.getsockname.return_value = ["192.168.1.105", 54321]
        mock_socket_cls.return_value = mock_sock

        ip = get_lan_ip()
        assert ip == "192.168.1.105"
        mock_sock.connect.assert_called_once_with(("8.8.8.8", 80))
        mock_sock.close.assert_called_once()


def test_get_lan_ip_fallback_on_exception():
    with patch("socket.socket") as mock_socket_cls:
        mock_sock = MagicMock()
        mock_sock.connect.side_effect = socket.error("Network unreachable")
        mock_socket_cls.return_value = mock_sock

        ip = get_lan_ip()
        assert ip == "127.0.0.1"


def test_quiz_landing_page_route(client):
    res = client.get("/quiz")
    assert res.status_code == 200


def test_quiz_direct_route(client):
    res = client.get("/quiz/CS501/quiz_01")
    assert res.status_code == 200


def test_api_quiz_get_existing(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        tmp_base = Path(tmpdir)
        quiz_dir = tmp_base / "01_Semester_1" / "CS501_Test" / "07_Quizzes_&_Anki"
        quiz_dir.mkdir(parents=True, exist_ok=True)
        sample_quiz = {
            "quiz_id": "test_quiz_01",
            "subject_id": "CS501_Test",
            "topic": "Neural Networks",
            "questions": [
                {
                    "id": "q1",
                    "question": "What is backprop?",
                    "options": ["Algorithm", "Fruit"],
                    "correct": 0,
                    "concept_id": "backprop"
                }
            ]
        }
        (quiz_dir / "test_quiz_01.json").write_text(json.dumps(sample_quiz), encoding="utf-8")

        monkeypatch.setattr(dashboard_app, "SEM1", tmp_base / "01_Semester_1")

        res = client.get("/api/quiz/CS501_Test/test_quiz_01")
        assert res.status_code == 200
        data = res.get_json()
        assert data["quiz_id"] == "test_quiz_01"
        assert len(data["questions"]) == 1

        # Should also work if requested with .json extension
        res_ext = client.get("/api/quiz/CS501_Test/test_quiz_01.json")
        assert res_ext.status_code == 200
        data_ext = res_ext.get_json()
        assert data_ext["quiz_id"] == "test_quiz_01"


def test_api_quiz_get_not_found(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        tmp_base = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "SEM1", tmp_base / "01_Semester_1")

        res = client.get("/api/quiz/NonExistentSubject/missing_quiz")
        assert res.status_code == 404
        data = res.get_json()
        assert "error" in data or "not found" in data.get("message", "").lower()


def test_api_quiz_submit_valid(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)

        payload = {
            "submission_uuid": "sub-api-test-1234",
            "subject_id": "CS501",
            "topic": "Search Algorithms",
            "summary": {
                "total": 2,
                "correct": 2,
                "wrong": 0,
                "percentage": 100.0,
                "avg_dwell_time_seconds": 12.5
            },
            "questions": [
                {
                    "id": "q1",
                    "concept_id": "bfs",
                    "is_correct": True,
                    "is_lucky_guess": False,
                    "dwell_time_seconds": 10.0
                }
            ]
        }

        res = client.post("/api/quiz/submit", json=payload)
        assert res.status_code == 200
        data = res.get_json()
        assert data.get("status") in ["success", "already_ingested"]


def test_api_quiz_submit_invalid_payload(client):
    # Non-json payload
    res = client.post("/api/quiz/submit", data="not json", content_type="text/plain")
    assert res.status_code == 400

    # Empty payload or missing submission_uuid
    res = client.post("/api/quiz/submit", json={})
    assert res.status_code == 400
    data = res.get_json()
    assert data.get("status") == "error"


def test_api_quiz_bookmarks_get_and_post(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        tmp_hub = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "HUB", tmp_hub)

        # GET initially when file doesn't exist
        res = client.get("/api/quiz/bookmarks")
        assert res.status_code == 200
        data = res.get_json()
        assert data == [] or data == {"bookmarks": []}

        # POST new bookmarks
        bookmarks = ["CS501_q1", "CS502_q3"]
        res_post = client.post("/api/quiz/bookmarks", json={"bookmarks": bookmarks})
        assert res_post.status_code == 200

        # GET updated bookmarks
        res_after = client.get("/api/quiz/bookmarks")
        assert res_after.status_code == 200
        data_after = res_after.get_json()
        assert (data_after == bookmarks) or (data_after.get("bookmarks") == bookmarks)

        # Also support posting direct list
        bookmarks_list = ["CS503_q5"]
        res_post_list = client.post("/api/quiz/bookmarks", json=bookmarks_list)
        assert res_post_list.status_code == 200

        res_after_list = client.get("/api/quiz/bookmarks")
        assert res_after_list.status_code == 200
        data_after_list = res_after_list.get_json()
        assert (data_after_list == bookmarks_list) or (data_after_list.get("bookmarks") == bookmarks_list)
def test_api_quiz_list(client):
    res = client.get("/api/quiz/list")
    assert res.status_code == 200
    data = res.get_json()
    assert "quizzes" in data
    assert isinstance(data["quizzes"], list)
    assert len(data["quizzes"]) >= 2
    topics = [q["topic"] for q in data["quizzes"]]
    assert any("Software" in t or "Crisis" in t or "Foundations" in t for t in topics)
def test_pwa_manifest_and_service_worker(client):
    res_manifest = client.get("/static/manifest.json")
    assert res_manifest.status_code == 200
    manifest = json.loads(res_manifest.get_data(as_text=True))
    assert manifest["short_name"] in ["MSCQuiz", "MCS Quiz", "MasterStudio"]
    assert manifest["display"] == "standalone"

    res_sw = client.get("/static/sw.js")
    assert res_sw.status_code == 200
    sw = res_sw.get_data(as_text=True)
    assert "CACHE_NAME" in sw
    assert "precache" in sw.lower()
    assert "quiz" in sw

def test_api_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "ok"
    assert "timestamp" in data
    assert "lan_ip" in data


def test_api_quiz_history(client):
    res = client.get("/api/quiz/history")
    assert res.status_code == 200
    data = res.get_json()
    assert "history" in data
    assert "summary" in data


def test_api_quiz_get_fuzzy_prefix(client):
    # Passing Quiz_01 should resolve Quiz_01_Software_Crisis
    res = client.get("/api/quiz/04_Advanced_Software_Eng/Quiz_01")
    assert res.status_code == 200
    data = res.get_json()
    assert "questions" in data
    assert len(data["questions"]) > 0


def test_api_quiz_bundle_success(client):
    tools_dir = BASE_DIR / "90_Shared_Toolbox" / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    from quiz_balancer import validate_schema_v2

    res = client.get("/api/quiz/bundle?semester=1")
    assert res.status_code == 200
    bundle = res.get_json()
    assert bundle["bundle_version"] == 2
    assert bundle["semester"] == 1
    assert bundle["total_quizzes"] >= 6
    assert len(bundle["quizzes"]) == bundle["total_quizzes"]
    assert "exported_at" in bundle

    for q in bundle["quizzes"]:
        valid, errors = validate_schema_v2(q)
        assert valid is True, f"Quiz {q.get('quiz_id')} failed validation: {errors}"
        assert len(q["questions"]) > 0


def test_pack_quiz_bundle_module():
    tools_dir = BASE_DIR / "90_Shared_Toolbox" / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    from pack_quiz_bundle import create_quiz_bundle

    bundle = create_quiz_bundle(semester=1, base_dir=BASE_DIR)
    assert bundle["bundle_version"] == 2
    assert bundle["semester"] == 1
    assert bundle["total_quizzes"] >= 6
    assert len(bundle["quizzes"]) == bundle["total_quizzes"]


def test_quiz_vault_asset_and_service_worker(client):
    res_vault = client.get("/static/quiz-vault.js")
    assert res_vault.status_code == 200
    vault_content = res_vault.get_data(as_text=True)
    assert "class QuizVault" in vault_content
    assert "MasterStudioQuizDB" in vault_content

    res_sw = client.get("/static/sw.js")
    assert res_sw.status_code == 200
    sw = res_sw.get_data(as_text=True)
    assert "master-studio-v" in sw
    assert "quiz-vault.js" in sw
    assert "/api/quiz/bundle" in sw


def test_api_quiz_import_from_mobile(client, monkeypatch):
    with TemporaryDirectory() as tmpdir:
        tmp_base = Path(tmpdir)
        monkeypatch.setattr(dashboard_app, "BASE", tmp_base)

        # Send quiz from mobile over LAN
        quiz_payload = {
            "subject_id": "04_Advanced_Software_Eng",
            "quiz_id": "Quiz_Telegram_Synced",
            "topic": "Telegram Received Lecture",
            "questions": [
                {
                    "id": "q1",
                    "concept_id": "telegram_sync",
                    "bloom_level": "Understand",
                    "question": "Was this quiz synced from Telegram over LAN?",
                    "question_ar": "هل تم استيراد هذا الكويز من تليغرام ومزامنته عبر الشبكة المحلية؟",
                    "options": ["Yes, flawlessly", "No", "Failed", "Unknown"],
                    "options_ar": ["نعم، بسلاسة تامة", "لا", "فشل", "غير معروف"],
                    "options_en": ["Yes, flawlessly", "No", "Failed", "Unknown"],
                    "answer": "A",
                    "correct": 0,
                    "explanation": "Seamless LAN sync between mobile PWA and PC agent."
                }
            ]
        }

        res = client.post("/api/quiz/import", json=quiz_payload)
        assert res.status_code == 200
        data = res.get_json()
        assert data["status"] == "success"
        assert len(data["imported"]) == 1

        # Verify file exists on PC storage in temporary base
        saved_file = tmp_base / "01_Semester_1" / "04_Advanced_Software_Eng" / "07_Quizzes_&_Anki" / "Quiz_Telegram_Synced.json"
        assert saved_file.exists()
        saved_data = json.loads(saved_file.read_text(encoding="utf-8"))
        assert saved_data["schema_version"] == 2
        assert saved_data["topic"] == "Telegram Received Lecture"


def test_post_quiz_web_share_target(client):
    from io import BytesIO
    quiz_json_bytes = json.dumps({
        "topic": "Shared via Telegram",
        "questions": [
            {
                "id": "q1",
                "concept_id": "share_target",
                "bloom_level": "Apply",
                "question": "Is Web Share Target active?",
                "question_ar": "هل ميزة مشاركة الويب نشطة؟",
                "options": ["Active", "Inactive", "Unknown", "Disabled"],
                "answer": "A",
                "correct": 0,
                "explanation": "Web Share Target POST handler receives files directly."
            }
        ]
    }).encode("utf-8")

    data = {
        "quiz_files": [(BytesIO(quiz_json_bytes), "Quiz_Shared.json")]
    }
    res = client.post("/quiz?shared=true", data=data, content_type="multipart/form-data")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "ms-shared-quizzes-data" in html
    assert "Shared via Telegram" in html
