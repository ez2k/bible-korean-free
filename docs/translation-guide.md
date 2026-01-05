# 어린이 성경 한글 번역 가이드라인

## 프로젝트 개요

**원본**: World English Bible (WEB) - Public Domain
**대상 연령**: 8-10세 (초등학교 저학년)
**번역 목표**: 어린이가 쉽게 이해할 수 있는 자연스러운 한국어 성경

---

## 번역 원칙

### 1. 어휘 선택
- **쉬운 단어 우선**: 어려운 한자어보다 쉬운 순우리말 사용
  - ❌ "창조하다" → ✅ "만들다"
  - ❌ "혼돈" → ✅ "아무것도 없는 상태"
  - ❌ "궁창" → ✅ "하늘"

- **추상적 개념은 구체적으로**:
  - ❌ "성령" → ✅ "하나님의 영"
  - ❌ "은혜" → ✅ "사랑과 도움"

### 2. 문장 구조
- **짧은 문장**: 한 문장에 하나의 생각
- **능동태 선호**: 피동태보다 능동태 사용
- **직접 화법 유지**: 대화는 생동감 있게

### 3. 어조
- **존댓말 사용**: "~했습니다", "~했어요"
- **따뜻하고 친근한 어조**: 딱딱한 문어체 피함
- **하나님은 항상 존칭**: "하나님께서", "말씀하셨어요"

### 4. 고유명사
| 영어 | 한글 |
|------|------|
| God | 하나님 |
| Lord | 주님 |
| Jesus | 예수님 |
| Christ | 그리스도 |
| Holy Spirit | 성령님 / 하나님의 영 |
| Moses | 모세 |
| Abraham | 아브라함 |
| David | 다윗 |
| Israel | 이스라엘 |

### 5. 어려운 개념 처리
괄호 안에 짧은 설명 추가:
- "만나(하늘에서 내린 음식)"
- "바리새인(유대교 지도자)"

---

## 번역 예시

### 원문 (WEB - Genesis 1:1-3)
> In the beginning, God created the heavens and the earth. The earth was formless and empty. Darkness was on the surface of the deep and God's Spirit was hovering over the surface of the waters. God said, "Let there be light," and there was light.

### 어린이용 한글 번역
> 맨 처음에 하나님께서 하늘과 땅을 만드셨어요. 그때 땅에는 아무것도 없었고, 깜깜한 어둠만 가득했어요. 하나님의 영이 물 위를 움직이고 계셨어요. 하나님께서 "빛이 생겨라!" 하고 말씀하시자, 빛이 생겼어요.

---

## 품질 체크리스트

번역 후 다음 항목을 확인하세요:

- [ ] 8세 어린이가 이해할 수 있는 단어인가?
- [ ] 문장이 너무 길지 않은가? (15단어 이하 권장)
- [ ] 하나님에 대한 존칭이 올바른가?
- [ ] 고유명사 표기가 일관적인가?
- [ ] 읽었을 때 자연스러운가?

---

## 파일 형식

### 입력 (source-web/json/*.json)
```json
{
  "type": "paragraph text",
  "chapterNumber": 1,
  "verseNumber": 1,
  "value": "In the beginning, God created..."
}
```

### 출력 (korean/*.json)
```json
{
  "book": "genesis",
  "bookKorean": "창세기",
  "chapter": 1,
  "verse": 1,
  "original": "In the beginning, God created...",
  "korean": "맨 처음에 하나님께서 하늘과 땅을 만드셨어요."
}
```

---

## 성경 책 목록

### 구약 (39권)
| 영어 | 한글 | 영어 | 한글 |
|------|------|------|------|
| Genesis | 창세기 | Ecclesiastes | 전도서 |
| Exodus | 출애굽기 | Song of Solomon | 아가 |
| Leviticus | 레위기 | Isaiah | 이사야 |
| Numbers | 민수기 | Jeremiah | 예레미야 |
| Deuteronomy | 신명기 | Lamentations | 예레미야애가 |
| Joshua | 여호수아 | Ezekiel | 에스겔 |
| Judges | 사사기 | Daniel | 다니엘 |
| Ruth | 룻기 | Hosea | 호세아 |
| 1 Samuel | 사무엘상 | Joel | 요엘 |
| 2 Samuel | 사무엘하 | Amos | 아모스 |
| 1 Kings | 열왕기상 | Obadiah | 오바댜 |
| 2 Kings | 열왕기하 | Jonah | 요나 |
| 1 Chronicles | 역대상 | Micah | 미가 |
| 2 Chronicles | 역대하 | Nahum | 나훔 |
| Ezra | 에스라 | Habakkuk | 하박국 |
| Nehemiah | 느헤미야 | Zephaniah | 스바냐 |
| Esther | 에스더 | Haggai | 학개 |
| Job | 욥기 | Zechariah | 스가랴 |
| Psalms | 시편 | Malachi | 말라기 |
| Proverbs | 잠언 | | |

### 신약 (27권)
| 영어 | 한글 | 영어 | 한글 |
|------|------|------|------|
| Matthew | 마태복음 | 1 Timothy | 디모데전서 |
| Mark | 마가복음 | 2 Timothy | 디모데후서 |
| Luke | 누가복음 | Titus | 디도서 |
| John | 요한복음 | Philemon | 빌레몬서 |
| Acts | 사도행전 | Hebrews | 히브리서 |
| Romans | 로마서 | James | 야고보서 |
| 1 Corinthians | 고린도전서 | 1 Peter | 베드로전서 |
| 2 Corinthians | 고린도후서 | 2 Peter | 베드로후서 |
| Galatians | 갈라디아서 | 1 John | 요한일서 |
| Ephesians | 에베소서 | 2 John | 요한이서 |
| Philippians | 빌립보서 | 3 John | 요한삼서 |
| Colossians | 골로새서 | Jude | 유다서 |
| 1 Thessalonians | 데살로니가전서 | Revelation | 요한계시록 |
| 2 Thessalonians | 데살로니가후서 | | |
