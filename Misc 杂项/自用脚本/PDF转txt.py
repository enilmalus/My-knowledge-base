import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    try:
        # 打开 PDF 文件
        reader = PdfReader(pdf_path)
        text = ""
        
        # 遍历每一页提取文本
        for page in reader.pages:
            text += page.extract_text()
        
        return text
    except Exception as e:
        print(f"发生错误: {e}")
        return ""

def save_text_to_txt(pdf_path, text):
    try:
        # 获取 PDF 文件的目录和文件名
        folder_path = os.path.dirname(pdf_path)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # 保存文本到 txt 文件（与 PDF 文件同路径）
        output_file = os.path.join(folder_path, f"{base_name}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        
        print(f"文本已保存到: {output_file}")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")

if __name__ == "__main__":
    # 替换为你的 PDF 文件路径
    pdf_path = "E:\BaiduNetdiskDownload\网络安全英语能力提升词汇手册-靶场导学包会员版.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    if text:
        save_text_to_txt(pdf_path, text)
    else:
        print("未提取到任何文本。")