import unicodedata

def print_all_emojis():
    """모든 이모지를 출력하는 함수"""
    print("=== 모든 이모지 목록 (복사 가능) ===")
    
    # 주요 이모지 유니코드 범위
    emoji_ranges = [
        (0x1F600, 0x1F64F),  # Emoticons (얼굴)
        (0x1F300, 0x1F5FF),  # Miscellaneous Symbols and Pictographs
        (0x1F680, 0x1F6FF),  # Transport and Map Symbols
        (0x1F1E0, 0x1F1FF),  # Regional Indicator Symbols (국기)
        (0x2600, 0x26FF),    # Miscellaneous Symbols
        (0x2700, 0x27BF),    # Dingbats
        (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
        (0x1F018, 0x1F270),  # Various symbols
    ]
    
    all_emojis = []
    
    for start, end in emoji_ranges:
        print(f"\n--- 범위: U+{start:X} - U+{end:X} ---")
        count = 0
        for code_point in range(start, end + 1):
            try:
                char = chr(code_point)
                # 이모지나 심볼인지 확인
                if unicodedata.category(char) in ['So', 'Sm', 'Sc', 'Sk'] or code_point >= 0x1F600:
                    print(f"{char}", end=" ")
                    all_emojis.append(char)
                    count += 1
                    if count % 20 == 0:  # 20개마다 줄바꿈
                        print()
            except ValueError:
                continue
        print(f"\n이 범위에서 {count}개의 이모지/심볼 발견")
    
    print(f"\n=== 전체 이모지 목록 (복사용) ===")
    print("다음 이모지들을 복사해서 사용하세요:")
    print()
    
    # 한 줄에 50개씩 출력
    for i, emoji in enumerate(all_emojis):
        print(emoji, end="")
        if (i + 1) % 50 == 0:
            print()
    
    print(f"\n\n총 {len(all_emojis)}개의 이모지가 출력되었습니다.")

def print_emoji_categories():
    """카테고리별 이모지 출력"""
    print("\n=== 카테고리별 이모지 ===")
    
    categories = {
        "얼굴": [0x1F600, 0x1F64F],
        "동물": [0x1F400, 0x1F4A3],
        "음식": [0x1F32E, 0x1F37F],
        "활동": [0x1F3A0, 0x1F3FF],
        "여행": [0x1F680, 0x1F6FF],
        "물건": [0x1F4A0, 0x1F4FF],
        "심볼": [0x2600, 0x26FF],
    }
    
    for category, (start, end) in categories.items():
        print(f"\n--- {category} ---")
        count = 0
        for code_point in range(start, end + 1):
            try:
                char = chr(code_point)
                if unicodedata.category(char) in ['So', 'Sm', 'Sc', 'Sk'] or code_point >= 0x1F600:
                    print(f"{char}", end=" ")
                    count += 1
                    if count % 15 == 0:
                        print()
            except ValueError:
                continue
        print(f"\n{category}: {count}개")

if __name__ == "__main__":
    print_all_emojis()
    print_emoji_categories()
