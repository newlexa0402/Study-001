import os
import sys
import base64
import zlib
import random
import string
from datetime import datetime
import shutil

class BasicObfuscator:
    def __init__(self, file_path, output_dir=None):
        self.file_path = os.path.abspath(file_path).replace('\\', '/')
        self.output_dir = output_dir or os.path.join(os.path.dirname(file_path), 'obfuscated')

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def obfuscate_code(self, code):
        # 코드를 압축하고 base64로 인코딩
        compressed = zlib.compress(code.encode())
        encoded = base64.b85encode(compressed)
        
        # 난독화된 코드를 실행할 wrapper 생성
        random_var = self.generate_random_string()
        wrapper = f"""
import base64
import zlib
{random_var} = {encoded}
exec(zlib.decompress(base64.b85decode({random_var})).decode())
"""
        return wrapper

    def obfuscate_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            obfuscated_code = self.obfuscate_code(code)
            
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
                
            output_path = os.path.join(self.output_dir, os.path.basename(self.file_path))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(obfuscated_code)
                
            print(f'성공: {self.file_path} 난독화 완료')
            print(f'출력 파일: {output_path}')
            return True
                
        except Exception as e:
            print(f'예외 발생: {str(e)}')
            return False

def main():
    try:


        file_path = r'C:\Quant Trading - Main\UI_main_window.py'


        
        # 파일 존재 확인
        if not os.path.exists(file_path):
            print(f'파일을 찾을 수 없음: {file_path}')
            return
            
        print("=== 기본 난독화 시작 ===")
        print(f'Python 버전: {sys.version}')
        print(f'작업 디렉토리: {os.getcwd()}')
        print(f'처리할 파일: {file_path}')
        
        obfuscator = BasicObfuscator(file_path)
        obfuscator.obfuscate_file()
        
    except Exception as e:
        print(f'프로그램 실행 중 오류 발생: {str(e)}')

if __name__ == "__main__":
    main()