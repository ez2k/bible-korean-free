# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

어린이용 한글 성경 번역 프로젝트입니다. World English Bible(WEB, Public Domain)을 8-10세 초등학교 저학년이 이해할 수 있는 한국어로 번역합니다.

## 프로젝트 구조

```
korean/           # 번역된 한글 성경 JSON 파일 (66권)
scripts/          # Python 유틸리티 스크립트
docs/             # 번역 가이드라인 및 품질 검토 보고서
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
          "original": "In the beginning...",
          "korean": "맨 처음에 하나님께서..."
        }
      ]
    }
  ]
}
```

긴 책(시편, 예레미야, 에스겔)은 `_part1`, `_part2` 등으로 분할됩니다.

## 번역 원칙 (핵심 요약)

1. **어휘**: 한자어 → 쉬운 순우리말 (예: "창조하다" → "만들다")
2. **문장**: 짧게, 한 문장에 하나의 생각
3. **어조**: 친근한 존댓말 ("~했어요", "~했습니다")
4. **하나님 존칭**: "하나님께서", "말씀하셨어요"
5. **어려운 개념**: 괄호 안에 짧은 설명 추가

자세한 가이드라인은 `docs/translation-guide.md` 참조.

## 스크립트 사용

```bash
# 파싱 스크립트 테스트 실행 (source-web/json 디렉토리 필요)
cd scripts && python parse_web.py
```

### 주요 함수 (scripts/parse_web.py)
- `parse_book(json_path)`: JSON에서 절(Verse) 추출
- `extract_chapter(json_path, chapter)`: 특정 장 추출
- `get_all_books(source_dir)`: 성경 순서대로 책 목록 반환
- `count_verses(json_path)`: 장별 절 수 계산

### 책 이름 매핑 (scripts/book_names.py)
- `BOOK_NAMES`: 영어→한글 매핑 딕셔너리
- `BOOK_ORDER`: 66권 정렬 순서 리스트
- `get_korean_name(english_name)`: 영어 책 이름을 한글로 변환

## 품질 검토 시 참고

`docs/translation-review-report.md`에 전체 번역본 품질 검토 결과가 있습니다:
- 어려운 한자어 목록과 권장 대체어
- 종교 용어 설명 방안
- 책별 주요 문제점

## 주의사항

- 원본 WEB 성경 파일(`source-web/`)은 별도 저장소에서 관리되며 gitignore됨
- 번역 시 대상 연령(8-10세)을 항상 고려
