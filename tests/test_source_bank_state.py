import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'90_Shared_Toolbox'/'tools'))
import quiz_bank_state as state
import quiz_source_gate


def test_source_null_keys_do_not_crash_or_dilute_practice_metrics(tmp_path, monkeypatch):
    directory=tmp_path/'01_Semester_1'/'04_Advanced_Software_Eng'/'07_Quizzes_&_Anki'
    directory.mkdir(parents=True)
    practice={'quiz_id':'Quiz_Ch01_T01_Test','questions':[{'answer':'A','question':'Plain?',
              'options':['aaa','bbb','ccc','ddd'],'options_ar':['أأأ','ببب','ججج','ددد']}]}
    source={'quiz_id':'Quiz_Ch01_S01_Source_MCQs','bank_kind':'source','questions':[
            {'answer':None,'correct':None,'question':'According to the lecture?',
             'options':['$x$','very long original source choice','c','d'],'options_ar':['س','أطول خيار في المصدر','ج','د']}]}
    for bank in (practice,source):
        (directory/(bank['quiz_id']+'.json')).write_text(json.dumps(bank),encoding='utf-8')
    monkeypatch.setattr(state,'BANKS_GLOB',str(directory/'*.json'))
    monkeypatch.setattr(quiz_source_gate,'validate_source_bank',lambda *a,**k:(True,[],[]))
    rows=state.read_vault()
    row=rows[('04_Advanced_Software_Eng',1)]
    assert row['banks']==2 and row['q']==2
    assert row['source_banks']==1 and row['source_q']==1 and row['source_ungraded']==1
    assert row['refs']==row['formula']==row['spread']==0
    text=state.render(rows,{('04_Advanced_Software_Eng',1):{'banks':2,'q':2}},1,'fixture',stamp=False)
    assert '**practice banks only**' in text
    assert 'Source track — local reviewed content' in text
