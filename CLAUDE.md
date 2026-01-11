# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

어린이용 한글 성경 번역 프로젝트입니다. World English Bible(WEB, Public Domain)을 8-10세 초등학교 저학년이 이해할 수 있는 한국어로 번역합니다.

- **원본**: World English Bible (WEB) - Public Domain
- **대상 연령**: 8-10세 (초등학교 저학년)
- **범위**: 전체 성경 66권 (구약 39권 + 신약 27권)
- **라이선스**: Public Domain (저작권 없음)
- **상태**: 번역 완료 (66/66권, 100%)

## 프로젝트 구조

```
bible-korean-free/
├── CLAUDE.md             # 이 파일 (AI 어시스턴트 가이드)
├── README.md             # 프로젝트 소개 및 진행 현황
├── .gitignore            # Git 무시 파일 설정
├── korean/               # 번역된 한글 성경 JSON 파일 (75개 파일)
│   ├── genesis.json
│   ├── psalms_part1.json # 긴 책은 분할됨
│   ├── psalms_part2.json
│   └── ...
├── scripts/              # Python 유틸리티 스크립트
│   ├── book_names.py     # 책 이름 영한 매핑
│   ├── parse_web.py      # JSON 파싱 및 절 추출
│   ├── fix_typos.py      # 오타 일괄 수정
│   ├── fix_particle_ga.py # 조사 오류 수정
│   └── fix_speech_style_*.py # 어투 일관성 수정 (6개 버전)
└── docs/                 # 문서
    ├── translation-guide.md        # 번역 가이드라인
    ├── translation-review-report.md    # 품질 검토 보고서 v1
    └── translation-review-report-v2.md # 품질 검토 보고서 v2 (최신)
```

## 데이터 형식

### 번역 파일 (korean/*.json)

```json
{
  "book": "genesis",
  "bookKorean": "창세기",
  "chapters": [
    {
      "chapter": 1,
      "verses": [
        {
          "verse": 1,
          "original": "In the beginning, God created the heavens and the earth.",
          "korean": "맨 처음에 하나님께서 하늘과 땅을 만드셨어요."
        }
      ]
    }
  ]
}
```

### 파일 분할 규칙

긴 책은 `_part1`, `_part2` 등으로 분할됩니다:
- `psalms_part1.json`, `psalms_part2.json`, `psalms_part3.json` (시편 150장)
- `jeremiah_part1.json`, `jeremiah_part2.json` (예레미야 52장)
- `ezekiel_part1.json`, `ezekiel_part2.json`, `ezekiel_part3.json` (에스겔 48장)
- `isaiah_part1.json`, `isaiah_part2.json` (이사야 66장)

## 번역 원칙

### 1. 어휘 선택
- **쉬운 단어 우선**: 어려운 한자어보다 쉬운 순우리말 사용
  - "창조하다" → "만들다"
  - "혼돈" → "아무것도 없는 상태"
  - "궁창" → "하늘"
- **추상적 개념은 구체적으로**:
  - "성령" → "하나님의 영"
  - "은혜" → "사랑과 도움"

### 2. 문장 구조
- 짧은 문장: 한 문장에 하나의 생각 (15단어 이하 권장)
- 능동태 선호: 피동태보다 능동태 사용
- 직접 화법 유지: 대화는 생동감 있게

### 3. 어조
- **존댓말 사용**: "~했어요", "~했습니다" 체
- 따뜻하고 친근한 어조
- **하나님은 항상 존칭**: "하나님께서", "말씀하셨어요"

### 4. 고유명사 규칙
| 영어 | 한글 |
|------|------|
| God / Yahweh / Lord | 하나님 |
| Jesus | 예수님 |
| Christ | 그리스도 |
| Holy Spirit | 성령님 / 하나님의 영 |

### 5. 어려운 개념 처리
괄호 안에 짧은 설명 추가:
- "만나(하늘에서 내린 음식)"
- "바리새인(유대교 지도자)"

자세한 가이드라인은 `docs/translation-guide.md` 참조.

## 스크립트 사용법

### 파싱 스크립트 (scripts/parse_web.py)

원본 WEB 성경 JSON을 파싱합니다. `source-web/json` 디렉토리가 필요합니다.

```bash
cd scripts && python parse_web.py
```

**주요 함수:**
- `parse_book(json_path)`: JSON에서 절(Verse) 추출
- `extract_chapter(json_path, chapter)`: 특정 장 추출
- `get_all_books(source_dir)`: 성경 순서대로 책 목록 반환
- `count_verses(json_path)`: 장별 절 수 계산

### 책 이름 매핑 (scripts/book_names.py)

영어-한글 책 이름 변환을 제공합니다.

```python
from book_names import get_korean_name, BOOK_NAMES, BOOK_ORDER

get_korean_name("genesis")  # "창세기"
get_korean_name("1corinthians")  # "고린도전서"
```

- `BOOK_NAMES`: 영어→한글 매핑 딕셔너리 (66권)
- `BOOK_ORDER`: 66권 정렬 순서 리스트
- `get_korean_name(english_name)`: 영어 책 이름을 한글로 변환

### 일괄 수정 스크립트

번역 품질 개선을 위한 일괄 수정 스크립트:

| 스크립트 | 용도 |
|----------|------|
| `fix_typos.py` | 오타 일괄 수정 |
| `fix_particle_ga.py` | 조사 오류 수정 ("하나님가" → "하나님께서" 등) |
| `fix_speech_style_*.py` | 어투 일관성 수정 (6단계 반복 개선) |
| `fix_speech_style_final.py` | 최종 어투 수정 (100+ 패턴) |

수정 스크립트 실행 예시:
```bash
cd scripts && python fix_speech_style_final.py
```

## 품질 검토

### 검토 보고서 위치

- `docs/translation-review-report.md`: 초기 품질 검토
- `docs/translation-review-report-v2.md`: 원문 대비 상세 검토 (최신)

### 주요 검토 기준

1. 원문 의미 전달 정확성
2. 번역 누락/오역 여부
3. 어린이 대상 적합성
4. 문법/철자 오류
5. 일관성 (어투, 용어)

### 과거 발견된 주요 오류 유형

| 오류 유형 | 예시 | 상태 |
|-----------|------|------|
| "하나님 하나님" 중복 | Yahweh God 번역 시 중복 | 수정됨 |
| "하나님는" 조사 오류 | 은/는 처리 오류 | 수정됨 |
| "하나님를" 조사 오류 | 을/를 처리 오류 | 수정됨 |
| "하나님가" 조사 오류 | 이/가 처리 오류 | 수정됨 |
| 어투 불일관 | "~다" vs "~어요" 혼재 | 수정됨 |

## 작업 시 주의사항

### 번역 수정 작업

1. **대상 연령(8-10세) 항상 고려**: 어려운 단어는 쉬운 말로 풀어쓰기
2. **조사 주의**: "하나님"은 받침이 없으므로 "하나님이", "하나님을", "하나님은" 사용
3. **어투 일관성**: "~해요" 체를 유지
4. **JSON 형식 유지**: 수정 후 JSON 유효성 검증 필요

### 일괄 수정 작업

1. 수정 전 백업 또는 git 상태 확인
2. 수정 통계 출력하여 변경 사항 확인
3. 수정된 파일 목록 기록

### 파일 처리

- 원본 WEB 성경 파일(`source-web/`)은 별도 저장소에서 관리되며 gitignore됨
- `korean/` 디렉토리의 JSON 파일은 UTF-8 인코딩
- JSON 파일 수정 시 들여쓰기 2칸 사용

## 일반적인 작업 흐름

### 특정 구절 찾기

```bash
# 특정 텍스트가 포함된 구절 찾기
grep -r "찾을텍스트" korean/

# 특정 책에서 찾기
grep "찾을텍스트" korean/genesis.json
```

### 일괄 문자열 치환

```python
import glob
import json

files = glob.glob('korean/*.json')
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('이전텍스트', '새텍스트')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
```

### 번역 품질 검증

```python
# 특정 패턴 검색
import glob
import re

files = glob.glob('korean/*.json')
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = re.findall(r'검색패턴', content)
    if matches:
        print(f"{filepath}: {len(matches)}건")
```

## 성경 책 순서 참조

### 구약 (39권)
창세기, 출애굽기, 레위기, 민수기, 신명기, 여호수아, 사사기, 룻기, 사무엘상, 사무엘하, 열왕기상, 열왕기하, 역대상, 역대하, 에스라, 느헤미야, 에스더, 욥기, 시편, 잠언, 전도서, 아가, 이사야, 예레미야, 예레미야애가, 에스겔, 다니엘, 호세아, 요엘, 아모스, 오바댜, 요나, 미가, 나훔, 하박국, 스바냐, 학개, 스가랴, 말라기

### 신약 (27권)
마태복음, 마가복음, 누가복음, 요한복음, 사도행전, 로마서, 고린도전서, 고린도후서, 갈라디아서, 에베소서, 빌립보서, 골로새서, 데살로니가전서, 데살로니가후서, 디모데전서, 디모데후서, 디도서, 빌레몬서, 히브리서, 야고보서, 베드로전서, 베드로후서, 요한일서, 요한이서, 요한삼서, 유다서, 요한계시록
