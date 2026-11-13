import copy
import hashlib
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '90_Shared_Toolbox' / 'tools'))
import quiz_source_gate as gate
from build_source_banks import scaffold_source_bank, split_into_batches

SID = '04_Advanced_Software_Eng'


def items(n=10):
    return [{'id':f'q{i}', 'concept_id':f'ase_source_ch01_q{i:02}', 'bloom_level':'Remember',
             'question':f'Original question {i}?', 'question_ar':f'السؤال الأصلي {i}؟',
             'options':['A','B','C','D'], 'options_en':['A','B','C','D'], 'options_ar':['أ','ب','ج','د'],
             'answer':'A', 'correct':0, 'explanation':'Original explanation.', 'explanation_ar':'الشرح الأصلي.',
             'source':{'id':f'1.{i}', 'reference':'Original reference', 'path':'source.md','line':1,
                       'key_status':'confirmed','note':{'ar':'ملاحظة','en':'Note'}}}
            for i in range(1,n+1)]


def make_bank(qs, batch=1):
    return scaffold_source_bank(SID, 'هندسة البرمجيات', 'د. علي', 'Dr. Ali', 1, batch, qs)


@pytest.mark.parametrize('n',[20,25,50])
def test_batches_preserve_approved_sizes_and_order(n):
    qs=items(n)
    batches=split_into_batches(qs)
    assert all(10<=len(b)<=15 for b in batches)
    assert [q for b in batches for q in b]==qs


def test_impossible_batch_size_is_not_silently_accepted():
    with pytest.raises(ValueError):
        split_into_batches(items(16))


def test_missing_key_is_not_replaced_with_A():
    qs=items()
    del qs[0]['answer']
    with pytest.raises(ValueError, match='guessing'):
        make_bank(qs)


def test_stable_concepts_and_nested_metadata_survive_batches():
    qs=items(20)
    originals=copy.deepcopy(qs)
    a,b=split_into_batches(qs)
    first,second=make_bank(a),make_bank(b,2)
    assert qs==originals
    assert second['questions'][0]['concept_id']=='ase_source_ch01_q11'
    assert second['questions'][0]['source']['id']=='1.11'
    assert first['questions'][0]['options']==['A','B','C','D']


def test_publication_checks_manifest_keys_and_original_hash(tmp_path, monkeypatch):
    monkeypatch.setattr(gate,'VAULT',tmp_path)
    root=tmp_path/'01_Semester_1'/SID
    root.mkdir(parents=True)
    source=root/'source.md'
    source.write_text('original source',encoding='utf-8')
    qs=items()
    bank=make_bank(qs)
    manifest={'schema_version':1,'review':'fixture reviewed','subject_id':SID,'sources':{'source.md':hashlib.sha256(source.read_bytes()).hexdigest()},
              'items':{q['source']['id']:{'question':q['question'],'options':q['options'],
                 'answer':q['answer'],'correct':q['correct'],'key_status':'confirmed',
                 'source_path':'source.md','source_line':1,'reference':'Original reference'} for q in qs}}
    assert gate.validate_source_bank(bank,manifest=manifest,check_publish=True)[0]
    bank['questions'][0]['answer']='B'
    bank['questions'][0]['correct']=1
    ok,errors,_=gate.validate_source_bank(bank,manifest=manifest,check_publish=True)
    assert not ok and any('reviewed source manifest' in e for e in errors)
    bank['questions'][0]['answer']='A'
    bank['questions'][0]['correct']=0
    source.write_text('changed source',encoding='utf-8')
    ok,errors,_=gate.validate_source_bank(bank,manifest=manifest,check_publish=True)
    assert not ok and any('original source file changed' in e for e in errors)
