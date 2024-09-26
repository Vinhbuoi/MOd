import zipfile

zip_name = input("Nhập tên file ZIP (bao gồm .zip): ")
file_to_zip = input("Nhập tên file cần nén (có dấu tiếng Việt): ")

with zipfile.ZipFile(zip_name, 'w') as zipf:
    zipf.write(file_to_zip)

print(f"Nén file '{file_to_zip}' thành '{zip_name}' thành công!")
