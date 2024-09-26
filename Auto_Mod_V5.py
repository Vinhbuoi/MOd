import getopt
import os
import sys
from termcolor import colored
import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
from os import listdir
import os
import getopt
import random
import re
from module import replace_slash, dump
from termcolor import *
from colorama import *
fixkhung=input(colored('[!] Fix Lag đầu trận:\n   [1] 100% (Dùng Trang phục mặc định hoặc bậc A để có hiệu ứng)\n   [2] 90% (Tất cả trang phục đều có hiệu ứng, khi sử dụng trang phục có hiệu ứng sẽ bị khựng đầu trận)\n>>> ','green'))
csimod = input(colored('[!] Mod Đầy Đủ Hiệu ứng (Rủi Ro): \n   [1] Có\n   [2] Không\n>>> ','green'))
def Function_Track_Guid(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, "rb") as r0:
            context = r0.read()
            Tracks = re.findall(rb'<Track trackName="(.*?)</Track>', context, re.DOTALL)
            if Tracks:
                for i in range(len(Tracks)):
                    trackName = Tracks[i]
                    guid_track = (re.findall(rb'guid="(.+?)" enabled', trackName)[0]).decode()
                    guid_true = str.encode(f'id="{i}" guid="{guid_track}"')
                    IdGuidFalse = re.findall(str.encode(rf'id="(.+?)" guid="{guid_track}"'), context)
                    if IdGuidFalse:
                        for j in range(len(IdGuidFalse)):
                            j = IdGuidFalse[j].decode()
                            guid_false = str.encode(f'id="{j}" guid="{guid_track}"')
                            context = context.replace(guid_false, guid_true)
        with open(file_path, "wb") as w0:
            w0.write(context)
            
import glob
from pathlib import *
try:
	import pyzstd
	import colorama
except:
	os.system('pip install pyzstd')
	os.system('pip install colorama')
	import pyzstd
	import colorama
os.system("clear")
print(colored("Chọn cơ chế Auto Mod:\n   [1] Nhận Ảnh Đầu Vào\n   [2] Nhận ID Đầu Vào",'yellow'))
inputask = input(colored("\n>>> ",'green'))
if not os.path.exists('idlist'):
        os.makedirs('idlist')
if inputask == '1':
	randominp = input(colored('[?] Bạn có muốn chọn ngẫu nhiên trang phục không? \n   [1] Có\n   [2] Không\n>>> ','green'))
	if randominp == '1':	
		idlist = os.listdir('list')
		grouped_numbers = {}
		for num in idlist:
			prefix = num[:3]
			if prefix not in grouped_numbers:
				grouped_numbers[prefix] = []
			grouped_numbers[prefix].append(num)
		
		random_numbers = []
		for prefix, nums in grouped_numbers.items():
			random_numbers.append(random.choice(nums))
		result_list = ' '.join(map(lambda x: x.split('.')[0],random_numbers))
		with open ('idlist.txt',"w") as e:
			e.write(result_list)
		with open ('idlist.txt','r') as listskinpic:
			input_numbers = listskinpic.read()
	else:
		print(colored('Đặt Ảnh Trang Phục cần Mod vào thư mục IDLIST','yellow'))
		input()
		idlist = os.listdir('idlist')
		result_list = ' '.join(map(lambda x: x.split('.')[0],idlist))
		with open ('idlist.txt',"w") as e:
			e.write(result_list)
		with open ('idlist.txt','r') as listskinpic:
			input_numbers = listskinpic.read()
elif inputask == '2':
	print(colored('Nhập SkinId cần Mod:','green'))
	input_numbers = input(colored('\n>>> ','green'))
else:
	print(colored('[HỆ THỐNG] Mặc Định chọn cơ chế [2]','green'))
	print(colored('Nhập SkinId cần Mod:','green'))
	input_numbers = input(colored('\n>>> ','green'))

#--------------------------------------------
def modsounddatabin(a):
	lujing = a
	idt0=int(IDCHECK[0:3]+'00')
	idt0 = idt0 - 1
	if IDCHECK in ['16707','13311']:
		if IDCHECK=='16707':
			idr0=int('1670703')
		if IDCHECK=='13311':
			idr0=int('1331102')
	else:
		idr0=int(IDCHECK)
	idr=(int(idr0)).to_bytes(8, byteorder='little').hex()
	idk=8
	idy=bytes(random.randbytes(idk))
	for k in range(21):
		idt0=idt0+1
		if idt0==idr0:
			continue
		else:
			idt=(int(idt0)).to_bytes(8, byteorder='little').hex()
			for i in os.listdir(lujing):
			    if i.endswith(".bytes"):
			        with open(lujing+'/'+'{}'.format(i), 'rb') as f:
			            contents = f.read()
			            a = contents.replace(bytes.fromhex(idt), idy).replace(bytes.fromhex(idr), bytes.fromhex(idt))
			            with open(lujing+'/'+'{}'.format(i), "wb") as w:
			                w.write(a)
def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_STORED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname)
                
def giaima(sanitized_input):
    def main() -> None:
        colorama.init()
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
        except getopt.GetoptError:
            usage()
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
        
        if not args:
            glob = Path(sanitized_input)
            args = glob.rglob("*")
                        
        args = set(args)
        for input_path in list(args):
            if os.path.isdir(input_path):
                args.discard(input_path)
                
                for entry in os.scandir(input_path):
                    if entry.is_file():
                        args.add(entry.path)
                        
        for input_path in args:
            input_blob = None
            try:
                with open(input_path, "rb") as f:
                    input_blob = f.read()
            except FileNotFoundError:
                continue
            
            if opts:
                opt, arg = opts[0]
            else:
                pos = input_blob.find(b"\x22\x4a\x67\x00")
                if pos != -1:
                   input_path = os.path.basename(input_path)
                   
                   opt = "-d"
                else:
                    opt = "-d"
            
            
            zstd_mode = None
            try:
                if opt in ("-d", "--decompress"):
                    input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                    zstd_mode = "decompress"
                    output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, False))

                output_path = input_path
                with open(output_path, "wb") as output_file:
                    output_file.write(output_blob)
            except pyzstd.ZstdError:
                continue
 


    if __name__ == "__main__":
            main()
    return
def nen(sanitized_input):
    def main() -> None:
        colorama.init()
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
        except getopt.GetoptError:
            usage()
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
        
        if not args:
            glob = Path(sanitized_input)
            args = glob.rglob("*")
                        
        args = set(args)
        for input_path in list(args):
            if os.path.isdir(input_path):
                args.discard(input_path)
                
                for entry in os.scandir(input_path):
                    if entry.is_file():
                        args.add(entry.path)
                        
        for input_path in args:
            input_blob = None
            try:
                with open(input_path, "rb") as f:
                    input_blob = f.read()
            except FileNotFoundError:
                continue
            
            if opts:
                opt, arg = opts[0]
            else:
                pos = input_blob.find(b"\x22\x4a\x67\x00")
                if pos != -1:
                   input_path = os.path.basename(input_path)
                   
                else:
                    if opts:
                        opt, arg = opts[0]
                    else:
                        pos = input_blob.find(b"\x22\x4a\x00\xef")
                        if pos != -1:
                        	continue
                        else:
                            if opts:
                                opt, arg = opts[0]
                            else:
                                def usage() -> None:
                                    print("\nUsage:\n\t{} [option] <file 1 path> <file 2 path> ...".format(sys.argv[0]))
                                    print("option:")
                                    print("\t-h, --help\t\tShow this")
                                    print("\t-c, --compress\t\tCompress Zstd")
                                    print("\t-d, --decompress\tDecompress Zstd")
                                ZSTD_DICT = b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
                                ZSTD_LEVEL = -999999 # or 19 idk
                                opt = "-c"
                                zstd_mode = None
                                if opt in ("-c", "--compress"):
                                    zstd_mode = "compress"
                                    output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))
                                    output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                                    output_blob[0:0] = b"\x22\x4a\x00\xef"
                                output_path = input_path
                                with open(output_path, "wb") as output_file:
                                    output_file.write(output_blob)


    if __name__ == "__main__":
            main()
def modages(directory_path):
	def get_sound_tick_id2(skinid: int):
		try:
		    return str(int(str(skinid), base=10) % 100)
		except BaseException as error:
			pass
	
	def playherosoundtick2(linesound: str, startsound: str, endsound: str, empty: str, sound_tick_id: str):
	    linesound = linesound.replace(startsound, empty)
	    linesound = linesound.replace(endsound, empty)
	    linesound = linesound.strip()
	    return linesound + '_Skin' + sound_tick_id
	
	def modifyline2(line, start, end, empty):
	    line = line.replace(start, empty)
	    line = line.replace(end, empty)
	    linelist = line.strip()
	    return linelist.split('/')
	    
	
	def skilleffect2(line, start, end, empty, heroid, skinid, resourceName = ['hero_skill_effects', 'Hero_Skill_Effects']):
	    linelist1 = modifyline2(line, start, end, empty)
	    linelist2 = []
	    con = ''
	    isindex = 0
	    for i, tmp in enumerate(linelist1):
	        if tmp in resourceName:
	            tmpidx = i + 1
	            if linelist1[tmpidx][0:3] == str(heroid)[0:3]:
	                if IDCHECK in ['16707','13311']:
	                    con += str(skinid)
	                else:
	                    con += linelist1[tmpidx] + '/' + str(skinid)
	                isindex += tmpidx
	            elif len(linelist1) == 3 and linelist1[1] in resourceName:
	                con += linelist1[i] + '/' + str(skinid)
	                isindex += i
	            else:
	                con += linelist1[0]
	    for i, tmp in enumerate(linelist1):
	        if i == isindex:
	            linelist2.append(con)
	        else:
	            linelist2.append(tmp)
	    return '/'.join(linelist2)
	
		        
		
	current_directory = directory_path
	empty = ''
	starts = ['<String name="resourceName" value="','<String name="prefab" value="','<String name="resourceName2" value="','<String name="resourceName3" value="','<String name="prefabName" value="']
	end = '" refParamName="" useRefParam="false" />'
	encoding = 'ISO-8859-1'
	soundfix001 = '<String name="eventName" value="'
	soundfix002 = '<bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false"/>\n        <String name="eventName" value="'
	startsound = '<String name="eventName" value="'
	endsound = '" refParamName="" useRefParam="false" />'
	efxfix = 'bAllowEmptyEffect" value="true'
	efxfix2 = 'bAllowEmptyEffect" value="false'
	normal = 'hero_skill_effects'
	componentline = 'component_effects'
	efxforce = '<String name="resourceName"'
	efxforce2 ='<bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false" />\n        <bool name="bForceIngoreCull" value="true" refParamName="" useRefParam="false" />\n        <String name="resourceName"'
	efxforce1 = '<bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\n        <bool name="bUseMasterSkinId" value="true" refParamName="" useRefParam="false" />\n        <bool name="bForceIngoreCull" value="true" refParamName="" useRefParam="false" />\n        <String name="resourceName"'
	heroid=IDCHECK[0:3]
	skinid=IDCHECK
	skinidfix=f'{skinid}/{skinid}/'
	skinidfix1=f'{skinid}/'
	skinidfull = '/{}/'.format(skinid)
	sound_tick_id = get_sound_tick_id2(skinid)
	#1 -> 6
	#2 -> 8
	#3 -> 9
	#4 -> 10
	#5 -> 7
	yenafix0=''
	yenafix='strReturnCityEffectPath'
	yenafix2='strReturnCityFall'
	csivirtual = 'CheckSkinIdVirtualTick'
	csinormal = 'CheckSkinIdTick'
	movebeam = 'MoveBeamDuration'
	triggerparticlefix = 'TriggerParticle'
	utgfix = 'bUseTargetSkinEffect" value="false'
	utgfix1 = 'bUseTargetSkinEffect" value="true'
	fuckairi2 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />\n      </Event>'.format(skinid)
	fuckairi = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n      </Event>'.format(skinid)
	csiairi = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	csiairimod = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	csiairivirtual = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	csiairivirtualmod ='<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />'
	csimod1 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n      </Event>'.format(skinid)
	csimod2 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />'.format(skinid)
	csimod3 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	csimod4 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'.format(skinid)
	csimod5 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	csimod6 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />\n      </Event>'
	csimod7 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />'
	csimod8 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="false" refParamName="" useRefParam="false" />'
	csimod9 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />'
	csimod10 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	bhtnfix = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'.format(skinid)
	bhtnfix1 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	bhtnfix2 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'.format(skinid)
	bhtnfix3 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	bhtnfix4 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'.format(skinid)
	bhtnfix5 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	bhtnfix6 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />'.format(skinid)
	bhtnfix7 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />'
	bhtnfix8 = '<int name="skinId" value="{}" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	bhtnfix9 = '<int name="skinId" value="99999" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
	cdn13015fix='<Condition id="22" guid="7e2cba5c-4dcd-4707-b5ce-81ec267ee8e6" status="false" />'
	cdn13015fix1='<Condition id="21" guid="41978040-eae0-449e-bd71-c2e0804b0515" status="false" />'
	fix11113='<Condition id="7" guid="92b36a35-ec2d-4a50-88e9-73f085da65d8" status="true" />'
	fixloi=''
	fix111132='"prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11113/sunshuangxiang_fly_spell_01"'
	fix111133='"prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11113/T3_sunshuangxiang_fly_spell_01"'
	fix15015='<Condition id="63" guid="e89a739d-ad18-433f-83c7-ed477652dd8f" status="true" />'
	fix150151='<Condition id="28" guid="c0b9dcbe-c83f-4a57-b203-70a202308416" status="true" />'
	fix150152='<Condition id="66" guid="bf4a4330-412d-4b5e-9a2f-723ba76bdffb" status="true" />'
	fix150153='<Condition id="39" guid="6e38b810-2c03-4c25-9331-fd09a03cb2e2" status="true" />'
	fix13112='<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/131_libai/13112/libai_buff_02" refParamName="" useRefParam="false" />'
	fix131121='<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/131_libai/13112/libai_buff_02" refParamName="" useRefParam="false" />\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/131_libai/13112/LiBai_buff_02_a" refParamName="" useRefParam="false" />\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/131_libai/13112/LiBai_buff_02_b" refParamName="" useRefParam="false" />'
	fix13210='<Condition id="14" guid="2a780e78-eb27-468a-aee5-3567a6e0debf" status="true" />'
	fix132101='<Condition id="12" guid="96ce198f-7350-4fca-871f-f733526e33b4" status="true" />'
	fix132102='<Condition id="13" guid="06d066af-7b8b-413c-8d4b-e0ccd1a289d4" status="true" />'
	fixefxsp='<bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />'
	fixefxsp1='<bool name="bApplySpecialEffect" value="false" refParamName="" useRefParam="false" />'
	fix15710='<String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_02" refParamName="" useRefParam="false" />'
	fix157101='<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/157_buzhihuowu/15710/huicheng_tongyong_02" refParamName="" useRefParam="false" />'
	fix157102='resourceName" value=""'
	fix157103='customTagName" value=""'
	fix14111='<Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />'
	fix141112='<Condition id="0" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />'
	fix141113='<String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b22" refParamName="" useRefParam="false" />'
	fix141114='''<String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b22" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="NoBuff" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="f1e30b20-0629-41f7-8e69-6fd22c3700d2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="1" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="BUFF" eventType="CheckSkillCombineConditionTick" guid="Buff" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fcff2124-c9e2-4380-a74b-13b666d35d71">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="b469b848-ce92-4676-a409-96de9fd62d05" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="28" guid="NoBuff" status="true" />
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="16a7d201-0703-4528-a017-d30aa65925a6">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="02a81b12-fdbe-4ff7-9401-d12e204df82a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="28" guid="NoBuff" status="true" />
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="65730ef4-3451-461e-a174-9379b6598c89">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b2" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="321f092c-3844-4f79-a951-7471f93abfdb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="29" guid="Buff" status="true" />
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="64489f20-b741-412b-b033-575e7c4f920b">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b11" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="bfa80bd3-3db9-4d1b-9ce5-ea4e66942853" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="29" guid="Buff" status="true" />
      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="false" />
      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="12033927-652b-467d-905f-b56d5c8e5b02">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b21" refParamName="" useRefParam="false" />'''
	fixrandom14111='<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_diaochan/14111/DiaoChan_attack_spell01_1_S" refParamName="" useRefParam="false" />'
	fixrandom141111='<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_diaochan/14111/DiaoChan_attack_spell01_1_S" refParamName="" useRefParam="false" />\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/141_diaochan/14111/DiaoChan_attack_spell01_1_S_B" refParamName="" useRefParam="false" />'
	csisearch = '"skinId" value="{}"'.format(skinid)
	animorg='<String name="clipName" value="'
	if IDCHECK in ['11107','12806','15704']:
		animmod='<String name="clipName" value="{}/'.format(IDCHECK)
	if IDCHECK in ['13311','16707']:
		componentid = IDCHECK +'_5'
		skinidreplacefix='<int name="skinId" value="{}" refParamName="" useRefParam="false" />'.format(skinid+'/'+componentid)
		skinidreplacefix2='<int name="skinId" value="{}" refParamName="" useRefParam="false" />'.format(skinid)
		if IDCHECK == '13311':
			soundcomponent = 'AW2'
		if IDCHECK == '16707':
			soundcomponent = 'AW3'
	

	output_path = os.path.join(current_directory)
	if csimod =="1":
		if IDCHECK in ['16707','11119']:
			pass
		else:
			for file in os.listdir(output_path):
				if file == 'P1.xml' and IDCHECK == '10620':
					continue
				elif file == 'S1.xml' and IDCHECK == '14111':
					continue
				elif file == 'U1.xml' and IDCHECK == '11113':
					continue
				elif file == 'U1.xml' and IDCHECK == '15015':
					continue
				elif IDCHECK == '13112' and file == 'S1E5.xml':
					continue
				elif file in ['S1B0.xml','S11B0.xml','S12B0.xml'] and IDCHECK == '13210':
					continue
				elif IDCHECK == '10611' and file == 'A2.xml':
					continue
				elif file == 'U1B2.xml' and IDCHECK == '13609':
					continue
				elif file == 'S3.xml' and IDCHECK == '15611':
					continue
				elif heroid == '533':
					continue
				elif IDCHECK == '50108' and file == 'S2B1.xml':
					continue
				elif IDCHECK == '50112' and file in ['P9.xml']:
					continue
				elif IDCHECK=="13011":
					continue
				file = os.path.join(output_path,file)
				try:
					with open(file,'r',-1) as w3:
						sex = w3.read()
					if 'CheckRandomRange' in sex and heroid not in ['106','157','116']:
						continue
					sex = sex.replace(csimod1,csimod6)
					sex = sex.replace(csimod2,csimod8)
					sex = sex.replace(csimod3,csimod9)
					sex = sex.replace(csimod4,csimod10)
					sex = sex.replace(csimod5,csimod7)
					if IDCHECK in['13015','13014']:
						sex=sex.replace(fuckairi,fuckairi2)
						sex=sex.replace(csiairi,csiairimod)
						sex=sex.replace(csiairivirtual,csiairivirtualmod)
					with open(file,'w',-1,encoding='utf-8') as w3:
						if IDCHECK=="15710":
							sex = sex.replace(fix15710, fix157101)
							sex = sex.replace(fix157102, fix157103)
							sex = sex.replace(fixefxsp, fixefxsp1)
						sex = sex.replace(efxfix, efxfix2)
						sex = sex.replace(utgfix,utgfix1)
						sex = sex.replace(yenafix,yenafix0)
						sex = sex.replace(yenafix2,yenafix0)
						sex=sex.replace(cdn13015fix,cdn13015fix1)
						w3.write(sex)
				except BaseException as error:
					continue
	for file in os.listdir(current_directory):
	    filepath = replace_slash(os.path.join(current_directory, file))
	    header = dump(filepath, encoding, __size=4)
	    if header == '\x22\x4A\x00\xEF':
	        continue
	    else:
	        newlists = []
	        lines = dump(filepath, encoding, mode=1)
	        for i, line in enumerate(lines):
	            for start in starts:
	                if re.search(start, line) and str(heroid)[0:3] in line:
	                    modified_content = skilleffect2(line, start, end, empty, heroid, skinid)
	                    newlists.append((i, modified_content))
	        if newlists:
	            content = dump(filepath, encoding, mode=1)
	            for i in range(len(newlists)):
	                content_index, modified_content = newlists[i]
	                for start in starts:
	                    try:
	                        if re.search(start, content[content_index]):
	                            indent = content[content_index].find(start)
	                            content[content_index] = (' ' * indent) + start + modified_content + end + '\n'
	                            
	                    except IndexError:
	                        continue
	            output_path = os.path.join(current_directory, file)
	            with open(output_path, 'w', -1, encoding) as w:
	                for line in content:
	                    if IDCHECK=='11113':
	                        line=line.replace(fix11113,fixloi)
	                        line=line.replace(fix111132,fix111133)
	                    if IDCHECK=='15015':
	                        line=line.replace(fix15015,fix150151)
	                        line=line.replace(fix150152,fix150153)
	                    if IDCHECK=='13112':
	                        line=line.replace(fix13112,fix131121)
	                    if IDCHECK=='13210':
	                        line=line.replace(fix13210,fixloi)
	                        line=line.replace(fix132101,fixloi)
	                        line=line.replace(fix132102,fixloi)
	                    if IDCHECK=='14111':
	                        line=line.replace(fix14111,fix141112)
	                        line=line.replace(fix141113,fix141114)
	                        line=line.replace(fixrandom14111,fixrandom141111)
	                    line= line.replace(skinidfix,skinidfix1)
	                    if IDCHECK=='15412':
	                        line= line.replace('Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/15413_HuaMuLan_Red','Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15413_HuaMuLan_Red')
	                    if IDCHECK=='13609':
	                        line= line.replace('        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />', '        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2" refParamName="" useRefParam="false" />').replace('        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />', '        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2_e" refParamName="" useRefParam="false" />')
	                        line= line.replace('<Vector3 name="scaling" x="1.300" y="1.000" z="1.000" refParamName="" useRefParam="false" />', '<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false" />')
	                    if IDCHECK=='13210':
	                        line= line.replace('\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_hurt_01" refParamName="" useRefParam="false" />', '\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_01" refParamName="" useRefParam="false" />\r        <String name="resourceName2" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_02" refParamName="" useRefParam="false" />\r        <String name="resourceName3" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_03" refParamName="" useRefParam="false" />')
	                    if heroid=='524':
	                        line= line.replace(f'prefab_skill_effects/hero_skill_effects/524_Capheny/{skinid}/Atk1_FireRange','prefab_skill_effects/hero_skill_effects/524_Capheny/Atk1_FireRange')
	                    if heroid=='537':
	                        line= line.replace('prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S',f'prefab_skill_effects/hero_skill_effects/537_Trip/{skinid}/Trip_attack_spell01_1_S')
	                    if heroid=='544':
	                        line= line.replace(f'prefab_skill_effects/hero_skill_effects/544_Painter/{skinid}/Painter_Atk4_blue','prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_blue').replace(f'prefab_skill_effects/hero_skill_effects/544_Painter/{skinid}/Painter_Atk4_red','prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_red')
	                    if IDCHECK in ['13311','16707']:
	                        line = line.replace(normal,componentline)
	                        line= line.replace(skinidfull,skinidfull+componentid+'/')
	                        line= line.replace(skinidreplacefix,skinidreplacefix2)
	                        line= line.replace(skinid+'/'+skinid+'/',skinid+'/')
	                    elif IDCHECK in ['11107','15704','12806']:
	                        line=line.replace(animorg,animmod)
	                    if fixkhung=='1':
	                        line=line.replace(efxforce,efxforce1)
	                    elif fixkhung=='2':
	                        line=line.replace(efxforce,efxforce2)
	                    else:
	                        line=line.replace(efxforce,efxforce1)
	                    w.write(line)
	  
	for file in os.listdir(current_directory):
	    filepath = replace_slash(os.path.join(current_directory, file))
	    header = dump(filepath, encoding, __size=4)
	    if header == '\x22\x4A\x00\xEF':
	        continue
	    else:
	        newlists = []
	        lines = dump(filepath, encoding, mode=1)
	        for i, linesound in enumerate(lines):
	            if startsound in linesound:
	                modified_content = playherosoundtick2(linesound, startsound, endsound, empty, sound_tick_id)
	                newlists.append((i, modified_content))
	        if newlists:
	            content = dump(filepath, encoding, mode=1)
	            for i in range(len(newlists)):
	                content_index, modified_content = newlists[i]
	                indent = content[content_index].find(startsound)
	                content[content_index] = (' ' * indent) + startsound + modified_content + endsound + '\n'
	            output_path = os.path.join(current_directory, file)
	            with open(output_path, 'w', -1, encoding) as w:
	                for linesound in content:
	                    linesound=linesound.replace('<bool name="useSkinSwitch" value="true','<bool name="useSkinSwitch" value="false')
	                    linesound= linesound.replace(soundfix001,soundfix002)
	                    if IDCHECK in ['13311','16707']:
	                        linesound = linesound.replace("Skin{}_Skin{}".format(sound_tick_id,sound_tick_id),"Skin{}".format(sound_tick_id))
	                        linesound=linesound.replace("Skin{}".format(sound_tick_id),"Skin{}".format(sound_tick_id)+"_"+soundcomponent)
	                    else:
	                        linesound = linesound.replace("Skin{}_Skin{}".format(sound_tick_id,sound_tick_id),"Skin{}".format(sound_tick_id))
	                    w.write(linesound)
def xml2bytes(a):
	
	def byteint(num):
	    return num.to_bytes(4, byteorder = 'little')
	
	skip=0
	DIR_PATH = a
	EXT = ['bytes']
	
	
	def bytestr(stri):
	    outbyte=byteint(len(stri)+4)
	    outbyte=outbyte+stri.encode()
	    return outbyte
	
	def byteattr(key,attr):
	    if key == 'Var':
	        if attr[key] == 'Array':
	            stri = 'JTArr'
	        elif attr[key] == 'String':
	            stri = 'JTPri'
	        else:
	            stri = 'JT' + attr[key]
	        aid = 6
	    elif key == 'Var_Raw':
	        stri = attr[key]
	        aid = 6
	    elif key == 'Type':
	        stri = 'Type' + attr[key]
	        aid = 8
	    elif key=='Type_Raw':
	    	stri=attr[key]
	    	aid=8
	    else:
	        import unicodedata
	        if unicodedata.numeric(key):
	            stri = attr[key]
	            aid = int(key)
	    stripro=stri.encode()
	    outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
	    return outbyte
	
	def bytenode(node):
	    iftex=False
	    if node.tag=='Item':
	        name1='Element'
	    else:
	        name1=node.tag
	    name=bytestr(name1)
	    attr1=b''
	    aindex=len(node.attrib)
	    plus=8
	    for key in node.attrib:
	        attr1=attr1+byteattr(key,node.attrib)
	    if (node.text!=None) and (node.text[0:1]!='\n'):
	        if node.text==' ':
	            stri1=''
	        else:
	        	stri1=node.text
	        iftex=True
	        stripro=('V'+stri1).encode()
	        attr1=attr1+byteint(len(stripro)+8)+byteint(5)+stripro+byteint(4)
	        aindex+=1
	        plus=4
	    attr1=byteint(len(attr1)+plus)+byteint(aindex)+attr1+byteint(4)
	    alchild=b''
	    if len(node):
	        cindex=0
	        for child in node:
	            alchild=alchild+bytenode(child)
	            cindex+=1
	        alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
	    else:
	    	if iftex==False:
	    		alchild=byteint(4)
	    bnode = name + attr1 + alchild
	    bnode = byteint(len(bnode)+4) + bnode
	    return bnode
	
	skip=0
	for file in listdir(DIR_PATH):
	    file_ext = file.split('.')[-1]
	    if file_ext in EXT:
	        byt= f'{a}/{file}'
	        tree=ET.parse(byt)
	        attr=b''
	        byt=bytenode(tree.getroot())
	        f=open(f'{a}/{file}','wb')
	        f.write(byt)
	        f.close()
def modassetref(a):   
	def modifyline(line, start, end, empty):
	    line = line.replace(start, empty)
	    line = line.replace(end, empty)
	    linelist = line.strip()
	    return linelist.split('/')
	
	def skilleffect(line, start, end, empty, heroid, IDCHECK, resourceName = ['hero_skill_effects', 'Hero_Skill_Effects']):
	    linelist1 = modifyline(line, start, end, empty)
	    linelist2 = []
	    con = ''
	    isindex = 0
	    for i, tmp in enumerate(linelist1):
	        if tmp in resourceName:
	            tmpidx = i + 1
	            if linelist1[tmpidx][0:3] == str(heroid)[0:3]:
	                if IDCHECK in ['16707','13311']:
	                    con += str(IDCHECK)
	                else:
	                    con += linelist1[tmpidx] + '/' + str(IDCHECK)
	                isindex += tmpidx
	            elif len(linelist1) == 3 and linelist1[1] in resourceName:
	                con += linelist1[i] + '/' + str(IDCHECK)
	                isindex += i
	            else:
	                con += linelist1[0]
	    for i, tmp in enumerate(linelist1):
	        if i == isindex:
	            linelist2.append(con)
	        else:
	            linelist2.append(tmp)
	    return '/'.join(linelist2)
	
		        
		
	current_directory = a
	empty = ''
	starts = ['<v1 Var="String" Type="System.String">prefab_skill','<v1 Var="String" Type="System.String">Prefab_Skill','<v1 Var="String" Type="System.String">prefab_skill_effects/hero_skill_effects/154_HuaMuLan/prefab','<v1 Var="String" Type="System.String">prefab_skill_effects/hero_skill_effects/533_HouYi/prefab','<v1 Var="String" Type="System.String">Project/Assets/Prefabs/Prefab']
	end = 'v1>'
	encoding = 'ISO-8859-1'
	heroid=IDCHECK[0:3]
	IDCHECKfull = '/{}/'.format(IDCHECK)
	normal = 'hero_skill_effects'
	componentline = 'component_effects'
	animorg='<v1 Var="String" Type="System.String">A'
	animorg2='<v1 Var="String" Type="System.String">S'
	if IDCHECK in ['11107','15704','12806']:
		animmod='<v1 Var="String" Type="System.String">{}/A'.format(IDCHECK)
		animmod2='<v1 Var="String" Type="System.String">{}/S'.format(IDCHECK)
	if IDCHECK in ['16707','13311']:
		componentid = IDCHECK+"_5"	

	for file in os.listdir(current_directory):
	    filepath = replace_slash(os.path.join(current_directory, file))
	    header = dump(filepath, encoding, __size=4)
	    if header == '\x22\x4A\x00\xEF':
	        continue
	    else:
	        newlists = []
	        lines = dump(filepath, encoding, mode=1)
	        for i, line in enumerate(lines):
	            for start in starts:
	                if re.search(start, line) and str(heroid)[0:3] in line:
	                    modified_content = skilleffect(line, start, end, empty, heroid, IDCHECK)
	                    newlists.append((i, modified_content))
	        if newlists:
	            content = dump(filepath, encoding, mode=1)
	            for i in range(len(newlists)):
	                content_index, modified_content = newlists[i]
	                for start in starts:
	                    try:
	                        if re.search(start, content[content_index]):
	                            indent = content[content_index].find(start)
	                            content[content_index] = (' ' * indent) + start + modified_content + end + '\n'
	                            
	                    except IndexError:
	                        continue
	            output_path = os.path.join(current_directory, file)
	            with open(output_path, 'w', -1, encoding) as w:
	                for line in content:
	                    line= line.replace(IDCHECK+'/'+IDCHECK+'/',IDCHECK+'/')
	                    if IDCHECK in ['16707','13311']:
	                        line = line.replace(normal,componentline)
	                        line= line.replace(IDCHECKfull,IDCHECKfull+componentid+'/')
	                    if IDCHECK in ['11107','12806','15704']:
	                        line=line.replace(animorg,animmod)
	                        line=line.replace(animorg2,animmod2)
	                    w.write(line)
	
	return
def bytes2xml(a):
	skip=0
	DIR_PATH = a
	EXT = ['bytes']
	
	def getint():
		return int.from_bytes(byt.read(4), 'little')
	
	def  getstr(pos=None):
		if pos is not None:
			byt.seek(pos, 0)
		ofs=getint()
		stri=byt.read(ofs-4)
		try:
			return stri.decode()
		except BaseException as error:
			pass
	
	def analynode(fid=None, sta=None):
		global i
		if sta==None:
			sta = byt.tell()
		else:
			byt.seek(sta, 0)
		ofs=getint()
		stri=getstr()
		if stri=='Element':
			stri1='Item'
		else:
			stri1=stri
		myid=i
		i=i+1
		byt.seek(4,1)
		aidx=getint()
		ite=False
		attr={}
		for j in range(0,aidx):
			attr1=analyattr()
			if type(attr1)==str:
				text1=attr1
				ite=True
			else:
				attr.update(attr1)
		if fid == None:
			nod[myid] = ET.SubElement(root, stri1, attrib=attr)
		else:
			nod[myid] = ET.SubElement(nod[fid], stri1, attrib=attr)
		if ite==True:
			if text1=='':
				nod[myid].text=' '
			else:
				nod[myid].text=text1
		checkfour()
		chk=sta+ofs-byt.tell()
		if chk>12:
			byt.seek(4,1)
			sidx=getint()
			for h in range (0,sidx):
				attr=analynode(myid,byt.tell())
		byt.seek(sta+ofs,0)
	
	def analyattr(pos=None):
		if pos==None:
			pos = byt.tell()
		else:
			byt.seek(pos, 0)
		ofs = getint()
		type = getint()
		if type == 5:
			stri = byt.read(ofs - 8).decode()[1:]
			checkfour()
			byt.seek(pos + ofs, 0)
			return stri
		else:
			if type == 6:
				stri = byt.read(ofs - 8).decode()
				if stri[0:2] == 'JT':
					if stri == 'JTArr':
						stri = 'Array'
					elif stri == 'JTPri':
						stri = 'String'
					else:
						stri = stri[2:]
					name = 'Var'
				else:
					name = 'Var_Raw'
			elif type == 8:
				stri2 = byt.read(ofs - 8).decode()
				if stri2[0:4]=='Type':
					stri=stri2[4:]
					name = 'Type'
				else:
					stri=stri2
					name='Type_Raw'
			else:
				try:
					stri = byt.read(ofs - 8).decode()
					name = str(type)
					byt.seek(pos + ofs, 0)
				except BaseException as error:
					pass
			try:
				return {name:stri}
			except BaseException as error:
				pass
	
	def checkfour():
		if getint()!=4:
			byt.seek(-4,1)
	for file in listdir(DIR_PATH):
	    file_ext = file.split('.')[-1]
	    if file_ext in EXT:
	        byt=open(f'{a}/{file}', 'rb')
	        i=0
	        nod={}
	        
	        ofs = getint()
	        stri = getstr()
	        if stri == 'Element':
	                stri1 = 'Item'
	        else:
	                stri1 = stri
	        byt.seek(4, 1)
	        aidx = getint()
	        ite = False
	        attr={}
	        for j in range(0, aidx):
	                attr1 = analyattr()
	                if type(attr1) == str:
	                        text1 = attr1
	                        ite = true
	                else:
	                    try:
	                        attr.update(attr1)
	                    except BaseException as error:
	                        pass
	                root = ET.Element(stri1, attrib=attr)
	        if ite == True:
	                nod[myid].text = text1
	        checkfour()
	        chk = ofs - byt.tell()
	        if chk > 12:
	                byt.seek(4, 1)
	                sidx = getint()
	                for h in range(0, sidx):
	                        analynode(None, byt.tell())
	        byt.close
	        
	        try:
	            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
		        
	            with open(f'{a}/{file}', "w" , encoding="utf-8") as f:
	                f.write(xmlstr)
	        except BaseException as error:
		        skip = skip+1
		        pass
VMODCHECK = 'deococainay'
chedovien = '1'
deskins = 'y'
fixlag= 'y'
def process_input_numbers(numbers):
    results = []

    for number in numbers:
        number_str = str(number)
        if len(number_str) == 5:
            results.append(number)
        else:
            print(f"Number {number} Is Invalid. Please Enter a 4 or 5 Digit Number ")
            return None
    
    return results

# Nhập các số từ người dùng
print("─"*30)
numbers = [int(num) for num in input_numbers.split()]

# Xử lý
results = process_input_numbers(numbers)

# In kết quả
if results is not None:
    # Sử dụng str.join để kết hợp các số thành một chuỗi
    result_str = ' '.join(map(str, results))
from colorama import init, Fore
from os import listdir
import os,zipfile,colorama,shutil,xml.dom.minidom,xml.sax,os,re,shutil,random,getopt,sys,pyzstd
ZSTD_DICT=b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
ZSTD_LEVEL = -99999999
ngoaihinhvaneov=b'/\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xd7\x0b\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x1c\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xcd\x01\x00\x00\x03\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhvaneovvang=b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhvaneovdo= b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhkhieov=b'B\x10\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xea\x0f\x00\x00\x0e\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa2\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Cam\x04\x00\x00\x00\x04\x00\x00\x00\xa3\x00\x00\x00\x19\x00\x00\x00ArtSkinLobbyShowMovie~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Movie\x04\x00\x00\x00\x04\x00\x00\x00Y\x00\x00\x00\x11\x00\x00\x00useNewMecanim<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x0f\x00\x00\x00bUnityLight<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00a\x00\x00\x00\x19\x00\x00\x00bUseCodeAnimComponent<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00f\x00\x00\x00\x08\x00\x00\x00MSAAR\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.EAntiAliasing\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x03\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xd2\x02\x00\x00\x05\x00\x00\x00\x8e\x00\x00\x00\x0b\x00\x00\x00Elementw\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Idle\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Loop\x04\x00\x00\x00\x04\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Run\x04\x00\x00\x00\x04\x00\x00\x00\x84\x00\x00\x00\x0b\x00\x00\x00Elementm\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/Dance_Effects/167/dance_03_texiao\x04\x00\x00\x00\x04\x00\x00\x00\x86\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00.\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.05998039\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.389713\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-2.490662\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xf9\x00\x00\x00\x03\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00xC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V1.831149E-07\x04\x00\x00\x00\x04\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00yC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V-8.35189E-09\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00z8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
CODEBIENVE=b'\r\n\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/huijidi_01" refParamName="" useRefParam="true"/>\r\n     <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
projack=b'      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">'
CODECHECKBIENVE = b''
checkHasteE1=b'\r\n    <Track trackName="CheckHeroIdTick1" eventType="CheckHeroIdTick" guid="Cre" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
checkHasteE1_leave=b'\r\n    <Track trackName="CheckHeroIdTick1" eventType="CheckHeroIdTick" guid="Cre" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
gtHasteE1bv=b'\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="412ea073-5944-46e4-ae5e-3037e855fda7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="5.000" isDuration="true">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
CODEBVYENA = b'\r\n\t<Track trackName="SetObjectDirectionTick2" eventType="SetObjectDirectionTick" guid="62996a6c-a8d4-42f6-90aa-6ee10271d08e" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="cc68e0b3-a496-4fc2-8128-6f215a965229">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="rotationY" value="180" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="ChangeHDHeightDuration3" eventType="ChangeHDHeightDuration" guid="3965e0e3-dd4b-44b8-ba36-682488d46550" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="ChangeHDHeightDuration" time="0.000" length="7.000" isDuration="true" guid="32824200-4e8e-4101-8d7d-be0ea0c313d1">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="heightChange" value="700" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="216618f0-8c39-4789-903b-08ddecb68b45" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="96fa9d23-90bd-480b-af17-a12d8c342396">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="clipName" value="Home2" refParamName="" useRefParam="false" />\r        <int name="layer" value="3" refParamName="" useRefParam="false" />\r        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />\r        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />\r        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="621e77cb-3dfc-40e3-8082-3e8603e3f7e2">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="clipName" value="Gohome2" refParamName="" useRefParam="false" />\r        <int name="layer" value="3" refParamName="" useRefParam="false" />\r        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="372cea2b-4677-4587-a037-9c13affdb97d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="007b4fc2-b841-493b-a390-91fde34a7624">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/huijidi_01_r" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticle" guid="3b9eb49a-febc-4403-827d-1dc93e40bf8b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="fba560da-156f-42fd-a4a0-b2d002e20c8b">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/huicheng_tongyong_01_r" refParamName="strReturnCityEffectPath" useRefParam="false" />\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe7\x8e\xaf\xe5\x88\x83\xe5\x8f\x8c\xe5\x89\x91buff" eventType="TriggerParticle" guid="b4915550-8c39-430e-a71c-71fbf46dfaa4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="8.367" isDuration="true" guid="2f0136b1-53ec-45e3-b28b-ba244e737c6f">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/Huicheng_ personality_01 _r" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="136fd4b7-a92f-4ba8-a3d6-d7c2fc6fbfe3" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="60a991c3-3bf1-4db0-b833-6f5fe406473b">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="born_back_reborn/huijidi_01_b" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticle" guid="ca420146-9732-4190-9790-c214efc6e549" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="37743f3e-8508-41df-9c61-5b44988c3889">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01_b" refParamName="strReturnCityEffectPath" useRefParam="false" />\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\x8c\xe5\x88\x83\xe5\x8f\x8c\xe5\x89\x91buff" eventType="TriggerParticle" guid="48412d98-0d6e-4772-bfca-fb58c57d741b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="8.367" isDuration="true" guid="3fff9929-dfc8-403b-9e63-510f08c4930a">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/Huicheng_ personality_01" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="ac18c450-19ac-42e1-8167-c194b96ba645" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="10bf2901-d739-46b0-a6bb-cbf8634011cc">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="born_back_reborn/huijidi_01_b" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
CODEBVYENA1 = b'\r\n\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="co1" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01" refParamName="" useRefParam="true"/>\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r     </Event>\r    </Track>\r    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="co1" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r      </Event>\r    </Track>\r\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="cod2" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01_r" refParamName="" useRefParam="true"/>\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r     </Event>\r    </Track>\r    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="cod2" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01_r" refParamName="" useRefParam="true"/>\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
GIATOC='13210,10611,11113,11604,13011,15004,16307,19007,50108,50112,54402,54004,13111,13112,13202,16606,19502,50605,53002,13311,13015,52011,15710'
GIATOCEDIT='11607,14111,15009,16707'
gtHasteE1 = gtHasteE1bv
gtHasteE1_leave = gtHasteE1bv
AABBCC = 'KunnAOV'
ngoaihinhxanhveres = b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhdoveres = b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'

def giai(a):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
    
    if not args:
        args = a
        input_blob = None
        with open(args, "rb") as f:
            input_blob = f.read()
        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "compress"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]
                zstd_mode = "decompress"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = args
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
            file_path = a
            test = os.path.isdir(file_path)
            file_stat = os.stat(file_path)
            new_atime = new_mtime = new_ctime = 4299999999
            os.utime(file_path, times=(new_atime, new_mtime))
            updated_stat = os.stat(file_path)
        except pyzstd.ZstdError:
            pass
    return
def ArtSkinLobbyIdleShowLOD(data4):
    a=camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD')-7
    a10=camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD')-3
    a3=camSkin[a:a+8]
    a4=a3[4:]
    a2=camSkin[a:a+4]
    vitri=int.from_bytes(a2,byteorder='little')
    ne=camSkin[vitri:]
    vitri2=int.from_bytes(a4,byteorder='little')
    a5=camSkin[a:a+vitri]
    a25=camSkin[a10:a10+vitri2]
    a22=camSkin[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyIdleShowLOD',b'\x00ArtLobbyIdleShowLOD')
    a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
    code=a5.replace(a25,a13)
    data4=len(code).to_bytes(4,byteorder='little')+code[4:]+ne
    return data4
def ArtPrefabLODnew(data):
    a=ab.find(b'\x00ArtPrefabLOD')-7
    a2=ab[a:a+4]
    a3=ab[a:a+5]
    a4=a3[4:5]#so 10
    vitri=int.from_bytes(a2,byteorder='little')
    data=ab[a:a+vitri]
    return data
def ArtPrefabLODExnew(data4):
    a=ab.find(b'\x00ArtPrefabLODEx')-7
    a2=ab[a:a+4]
    a3=ab[a:a+5]
    a4=a3[4:5]#so 10
    vitri=int.from_bytes(a2,byteorder='little')
    data4=ab[a:a+vitri]
    return data4
def ArtSkinPrefabLODnew(data3):
    a=ab.find(b'\x00ArtSkinPrefabLOD')-7
    a10=ab.find(b'\x00ArtSkinPrefabLOD')-3
    a3=ab[a:a+8]
    a4=a3[4:]
    a2=ab[a:a+4]
    vitri=int.from_bytes(a2,byteorder='little')
    vitri2=int.from_bytes(a4,byteorder='little')
    a5=ab[a:a+vitri]
    a25=ab[a10:a10+vitri2]
    a22=ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD',b'\x00ArtPrefabLOD')
    a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
    code=a5.replace(a25,a13)
    data3=len(code).to_bytes(2,byteorder='little')+code[2:]
    return data3 
def ArtSkinPrefabLODExnew(data2):
    a=ab.find(b'\x00ArtSkinPrefabLODEx')-7
    a10=ab.find(b'\x00ArtSkinPrefabLODEx')-3
    a3=ab[a:a+8]
    a4=a3[4:]
    a2=ab[a:a+4]
    vitri=int.from_bytes(a2,byteorder='little')
    vitri2=int.from_bytes(a4,byteorder='little')
    a5=ab[a:a+vitri]
    a25=ab[a10:a10+vitri2]
    a22=ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLODEx',b'\x00ArtPrefabLODEx')
    a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
    code=a5.replace(a25,a13)
    data2=len(code).to_bytes(4,byteorder='little')+code[4:]
    return data2
def bienve(data):#Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    IDBV1=IDCHECK.encode()
    codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    codenew3=codenew1.replace(b'Name_Hero',teninfo23)
    data=codenew3.replace(b'ID_Skin',IDBV1)
    return data
def bienve1(data):#Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    IDBV1=IDCHECK.encode()
    codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    data=codenew1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/',b'prefab_skill_effects/component_effects/16707/16707_5/')
    return data
def bienvecheck(data):
    teninfobv1=NAME_HERO[4:].encode()
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    CODECHECKBIENVE=b'      </Event>\r\n    </Track>\r\n    <Track trackName="CheckHeroIdTick0" eventType="CheckHeroIdTick" guid="Cre" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">'

    codenew=CODECHECKBIENVE.replace(b'value="ID_Hero',b'value="'+IDBV)
    data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    return data
def hasteE1(data):
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    IDBV1=IDCHECK.encode()
    codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    codenew3=codenew1.replace(b'Name_Hero',teninfo23)
    data=codenew3.replace(b'ID_Skin',IDBV1)
    return data 
def hasteE1check(data):
    teninfobv1=NAME_HERO[4:].encode()
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    IDBV=IDBV
    codenew=data.replace(b'value="ID_Hero',b'value="'+IDBV)
    data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    return data
def hasteE1_leave(data):
    teninfo23=NAME_HERO.encode()
    IDBV=IDCHECK[:3].encode()
    IDBV1=IDCHECK.encode()
    codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    codenew3=codenew1.replace(b'Name_Hero',teninfo23)
    data=codenew3.replace(b'ID_Skin',IDBV1)
    return data 
def hasteE1check_leave(data):
    teninfobv1=NAME_HERO[4:].encode()
    teninfo23=NAME_HERO.encode()
    IDBV=heroid.encode()
    codenew=data.replace(b'value="ID_Hero',b'value="'+IDBV)
    data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
    return data
def count_tracks_above_action_name(filename, action_name):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        if action_name in line:
            break
        if 'trackName' in line:
            count += 1
    return count
IDD = result_str
IDMODSKIN=IDD.split()
IDMODSKIN1=IDD.split()
print(f"Pack {len(numbers)} Skin")
print("─"*30)
if len(numbers) == 0:
	print(colored('Không có Skin nào được chọn!','red'))
	exit()
DANHSACH = IDD.split()
with open ('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
    a=f.read()
if b'"J\x00' in a:
    giai('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes')
map1='Resources/1.55.1/Languages/VN_Garena_VN/languageMap.txt'
map2='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_Newbie.txt'
map3='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_WorldConcept.txt'
map4='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_Xls.txt'
map5='Resources/1.55.1/Languages/VN_Garena_VN/lanMapIncremental.txt'
FILES_MAP = [map1, map2, map3, map4, map5]
for mapp in FILES_MAP:
    with open (mapp, 'rb') as f:
        a=f.read()
    if b'"J\x00' in a:
        giai(mapp)
TENSKIN =[]
for mapp in FILES_MAP:
    for i in DANHSACH:

        with open(mapp,'rb') as f: rpl=f.read()
        with open('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes','rb') as f: RPL=f.read()
        i = int(i)
        IDFIND=RPL.find(i.to_bytes(4,'little')+int(str(i)[:3]).to_bytes(4,'little'))
        if IDFIND != -1:
            VT=RPL[IDFIND+12:IDFIND+31]
            VT1=rpl.find(VT)
            VT2=rpl.find(b'\r',VT1)
            VTR=rpl[VT1:VT2]
            VT=RPL[IDFIND+40:IDFIND+59]
            VT1=rpl.find(VT)
            VT2=rpl.find(b'\r',VT1)
            VTR_SKIN=rpl[VT1:VT2]
            A = VTR[22:]
            B = VTR_SKIN[22:]
            #aaaa=(' '.join(all_characters))
            sanitized_input = ((A + b' ' +B).decode())
            sanitized_input = ''.join(char for char in sanitized_input if char not in ['/', '\\', ':', '*', '?', '"', '<', '>', '|'])
            TENSKIN.append(sanitized_input)
#print(TENSKIN)
aaabbbcccnnn = ''
if os.path.exists('skinlist.txt'):
	os.remove('skinlist.txt')
for sanitized_input in TENSKIN:
    if sanitized_input == ' ':
        continue
        
    if '[ex]' in sanitized_input:
        continue
        
    else:
        print(colored(sanitized_input,"yellow"))
        aaabbbcccnnn = sanitized_input
        sanitized_input = sanitized_input+"KunnAOV"

        with open('skinlist.txt', 'a', encoding='utf-8') as file:
            file.write(aaabbbcccnnn+'\n')
tinhtime = len(numbers)*20
tinhskin = len(numbers)
tinhskin0 = 0
sanitized_input = aaabbbcccnnn
giai('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes')
print('─'*30)
if len(DANHSACH) > 1:
    sanitized_input = input('Enter Skin Pack Name: ')
if tinhtime<60:
	print(colored(f'Tiến hành Mod, Thời gian ước tính {tinhtime} giây.','yellow'))
if tinhtime>=60:
	tinhtime=tinhtime//60
	print(colored(f'Tiến hành Mod, Thời gian ước tính {tinhtime} phút.','yellow'))
print('─'*30)
if os.path.exists(sanitized_input):
	shutil.rmtree(sanitized_input)
#===================================================================================================================
base_path = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/"
directories = ["Actor", "Shop", "Sound", "Skill", "Character", "Motion", "Global"]
for directory in directories:
    os.makedirs(os.path.join(base_path, directory), exist_ok=True)
    
#===================================================================================================================
print(colored('Tiến hành Sao Chép tệp tin, xin chờ...','green'))
file_actor = "Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes"
file_actor_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes"
shutil.copy(file_actor, file_actor_mod)
giai(file_actor_mod)

file_shop = "Resources/1.55.1/Databin/Client/Shop/HeroSkinShop.bytes"
file_shop_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Shop/HeroSkinShop.bytes"
shutil.copy(file_shop, file_shop_mod)
giai(file_shop_mod)
file_sound0 = "Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
file_sound_mod0 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
shutil.copy(file_sound0, file_sound_mod0)
giai(file_sound_mod0)
file_sound1 = "Resources/1.55.1/Databin/Client/Sound/BattleBank.bytes"
file_sound_mod1 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/BattleBank.bytes"
shutil.copy(file_sound1, file_sound_mod1)
giai(file_sound_mod1)

file_sound2 = "Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
file_sound_mod2 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
shutil.copy(file_sound2, file_sound_mod2)
giai(file_sound_mod2)

file_sound3 = "Resources/1.55.1/Databin/Client/Sound/HeroSound.bytes"
file_sound_mod3 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/HeroSound.bytes"
shutil.copy(file_sound3, file_sound_mod3)
giai(file_sound_mod3)

file_sound4 = "Resources/1.55.1/Databin/Client/Sound/LobbyBank.bytes"
file_sound_mod4 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/LobbyBank.bytes"
shutil.copy(file_sound4, file_sound_mod4)
giai(file_sound_mod4)

file_sound5 = "Resources/1.55.1/Databin/Client/Sound/LobbySound.bytes"
file_sound_mod5 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/LobbySound.bytes"
shutil.copy(file_sound5, file_sound_mod5)
giai(file_sound_mod5)

file_sound6 = "Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
file_sound_mod6 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
shutil.copy(file_sound6, file_sound_mod6)
giai(file_sound_mod6)

Sound_Files = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound"

file_skill1 = "Resources/1.55.1/Databin/Client/Skill/liteBulletCfg.bytes"
file_mod_skill1 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Skill/liteBulletCfg.bytes"
shutil.copy(file_skill1, file_mod_skill1)
giai(file_mod_skill1)

file_skill2 = "Resources/1.55.1/Databin/Client/Skill/skillmark.bytes"
file_mod_skill2 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Skill/skillmark.bytes"
shutil.copy(file_skill2, file_mod_skill2)
giai(file_mod_skill2)

file_Modtion = "Resources/1.55.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
file_mod_Modtion = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
shutil.copy(file_Modtion, file_mod_Modtion)
giai(file_mod_Modtion)

file_vien = "Resources/1.55.1/Databin/Client/Global/HeadImage.bytes"
file_mod_vien = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Global/HeadImage.bytes"
shutil.copy(file_vien, file_mod_vien)
giai(file_mod_vien)

with zipfile.ZipFile('Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes') as f:
    f.extractall(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/')
    giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml')
    f.close()

file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
action_name = '<String name="actionName" value="Back"'
track_count = count_tracks_above_action_name(file_name, action_name)
track_count = track_count - 1
k1bv=track_count
track_count1 = k1bv+1

giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml')
file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml'
action_name = '</Project>'
track_count = count_tracks_above_action_name(file_name, action_name)
hasteE1cechbv = track_count
giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml')

giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml')
file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml'
action_name = '</Project>'
track_count = count_tracks_above_action_name(file_name, action_name)
hasteE1_leavecechbv = track_count
giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml')

giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE2.xml')
file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE2.xml'
action_name = '</Project>'
track_count = count_tracks_above_action_name(file_name, action_name)
hasteE2cechbv = track_count
giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE2.xml')

giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE3.xml')
file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE3.xml'
action_name = '</Project>'
track_count = count_tracks_above_action_name(file_name, action_name)
hasteE3cechbv = track_count
giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE3.xml')

os.makedirs(f"{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/")
shutil.copy('Resources/1.55.1/Databin/Client/Character/ResComponentMeshReplace.bytes',f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Character/ResCharacterComponent.bytes")
print(colored('[✓] Sao Chép tệp tin thành công, Tiến Hành Mod...','yellow'))
#===================================================ICON_BAC================================================================

for IDMODSKIN in IDMODSKIN:
    nhap_id = IDMODSKIN
    file_actor = file_actor_mod
    file_shop = file_shop_mod
    IDCHECK = IDMODSKIN
    IDSOUND_S = IDMODSKIN
    phukien = ''
    phukienv = ''

    if IDSOUND_S[3:4] == '0':
        IDSOUND_S=IDSOUND_S[:3]+IDSOUND_S[4:]
    IDSOUND1=IDSOUND_S[3:]
    IDSOUND12=IDSOUND1.encode()
    IDSOUND = b"_Skin" + IDSOUND12
    HPCAO=b'\r\n    <!-- '+AABBCC.encode('utf-8') +b' -->'

    IDINFO=int(IDMODSKIN)+1
    IDINFO=str(IDINFO)
    if str(IDINFO)[3:4] == '0':
        IDINFO=IDINFO[:3]+IDINFO[4:]
    IDINFO=str(IDINFO)
    if IDCHECK not in ["10611", "13211", "13212"]:
        def tim_id(data, chuoi_thay_the):
            id_tim = b'\x00\x00' + int(data).to_bytes(4, 'little')
            
            vi_tri_truoc = chuoi_thay_the.find(id_tim) - 2
            
            vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
            vi_tri_tim = int.from_bytes(vi_tri, 'little')
            if vi_tri_tim > 100:
                return True
            else:
                return False

        tat_ca_id = []
        with open(file_actor, 'rb') as f:
            chuoi_thay_the = f.read()


        for i in range(int(nhap_id[:3] + '00'), int(nhap_id[:3] + '99')):
            if i != int(nhap_id):
                kiem_tra_id = tim_id(i, chuoi_thay_the)
                if kiem_tra_id:
                    tat_ca_id.append(str(i))

        id_skin_moi = list(set(tat_ca_id))

        vi_tri_id_tim_kiem = b'\x00\x00' + int(nhap_id).to_bytes(4, 'little')
        vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 2
        vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
        vi_tri_tim = int.from_bytes(vi_tri, 'little')
        vi_tri_mod = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]

        for i in id_skin_moi:
            ll = i
            vi_tri_mod1 = vi_tri_mod
            vi_tri_id_tim_kiem = b'\x00\x00' + int(i).to_bytes(4, 'little')
            vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 2
            vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
            vi_tri_tim = int.from_bytes(vi_tri, 'little')
            vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]

            if i[3:] == '00':
                if vi_tri_mod1[64:65] == b'\x07':
                    i = nhap_id[:3] + nhap_id[4:]
                    vi_tri_mod1 = vi_tri_mod1[:68] + vi_tri_mod1[68:73] + b'0' + vi_tri_mod1[74:]
                    vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]
                    vi_tri_mod1 = vi_tri_mod1[:36] + b'\x00' + vi_tri_mod1[37:]
                else:
                    vi_tri_mod1 = vi_tri_mod1[:68] + vi_tri_mod1[68:73] + b'0' + vi_tri_mod1[75:]
                    vi_tri_mod1 = (len(vi_tri_mod1[:64] + b'\x07' + vi_tri_mod1[65:]) - 4).to_bytes(4, 'little') + vi_tri_mod1[4:64] + b'\x07' + vi_tri_mod1[65:]
                    vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]
                    vi_tri_mod1 = vi_tri_mod1[:36] + int(ll[3:]).to_bytes(1, 'little') + vi_tri_mod1[37:]
            else:
                vi_tri_mod1 = vi_tri_mod1[:36] + int(i[3:]).to_bytes(1, 'little') + vi_tri_mod1[37:]
                vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]

            chuoi_thay_the = chuoi_thay_the.replace(vi_tri, vi_tri_mod1).replace(b'\x07\x00\x00\x00301330_2', b'\x07\x00\x00\x00301330').replace(b'\x07\x00\x00\x003016702', b'\x07\x00\x00\x00301670').replace(b'$\x03\x00\x00\xf43', b'"\x03\x00\x00\xf43').replace(b'g\x03\x00\x00<A', b'f\x03\x00\x00<A').replace(b'73F8D70E20CB6B44_##\x00\x00\x00\x00\x00\x14\x00\x00\x00C748BCA5990E9431_##\x00\x07\x00\x00\x00301330', b'73F8D70E20CB6B44_##\x00\x00\x00\x00\x00\x14\x00\x00\x00C748BCA5990E9431_##\x00\x07\x00\x00\x00301320')  # 13311and16707

        with open(file_actor, 'wb') as f:
            f.write(chuoi_thay_the)
        dieukienmod = vi_tri_mod1
        tat_ca_id_skin = []
        with open(file_shop, 'rb') as f:
            chuoi_thay_the = f.read()


        for id_tim in range(int(nhap_id[:3] + '00'), int(nhap_id[:3] + '99')):
            if str(id_tim) == nhap_id:
                continue
            vi_tri_id_tim_kiem = id_tim.to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14'
            if chuoi_thay_the.find(vi_tri_id_tim_kiem) != -1:
                tat_ca_id_skin.append(vi_tri_id_tim_kiem)

        if chuoi_thay_the.find(int(nhap_id).to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14') != -1:
            vi_tri_id_tim_kiem = int(nhap_id).to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14'
            vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 4
            vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
            vi_tri_tim = int.from_bytes(vi_tri, 'little')
            ma_skin_mod = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]
            for id1 in tat_ca_id_skin:
                vi_tri_truoc = chuoi_thay_the.find(id1) - 4
                vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
                vi_tri_tim = int.from_bytes(vi_tri, 'little')
                ma_skin_mod1 = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]
                ma_rpl = ma_skin_mod[:4] + id1[:4] + ma_skin_mod[8:]
                chuoi_thay_the = chuoi_thay_the.replace(ma_skin_mod1, ma_rpl)

        with open(file_shop, 'wb') as f:
            f.write(chuoi_thay_the)
    if IDCHECK in ["10611", "13211", "13212"]:
        
        
        ID = IDCHECK
        IDB = int(ID).to_bytes(4, byteorder="little")
        IDH = int(ID[0:3]).to_bytes(4, byteorder="little")
        Files = [file_actor, file_shop]
        a = 1
        for File in Files:
            All = []
            Skin = ""
            file = open(File, "rb")
            Code = file.read()
            Find= -10
            while True:
                Find = Code.find(b"\x00\x00"+IDH, Find+10)
                if Find == -1: break
                elif str(int.from_bytes(Code[Find-2:Find], byteorder="little"))[0:3] == ID[0:3]:
                    VT2 = int.from_bytes(Code[Find-6:Find-4], byteorder="little")
                    Code2 = Code[Find-6:Find-6+VT2]
                    All.append(Code2)
                    if Code2.find(IDB) != -1: Skin=Code2
            for Id in All:
                Cache = Skin.replace(Skin[4:6], Id[4:6], 1)
                Cache = Cache.replace(Cache[35:44], Id[35:40]+Cache[40:44],1)
                Hero = hex(int(ID[0:3]))[2:]
                if len(Hero) == 3: Hero = Hero[1:3] + "0" + Hero[0]
                else: Hero+="00"
                Hero += "0000"
                Hero = bytes.fromhex(Hero)
                Cache = Cache.replace(Cache[8:12],Hero,1)
                if File == Files[0]:
                    if Id == All[0]:
                        ID30 = b"\x07\x00\x00\x0030" + bytes(ID[0:3] + "0", "utf8") + b"\x00"
                        XYZ = Cache[64]
                        ID0 = Cache[64: 68 + XYZ]
                        Cache = Cache.replace(ID0, ID30, 1)
                        VT = Id.find(b"Hero_")
                        NumHero = Id[VT - 4]
                        Hero = Id[VT - 4: VT + NumHero]
                        Cache = Cache.replace(b"jpg\x00\x01\x00\x00\x00\x00", b"jpg\x00" + Hero)
                        Full = Cache.count(Hero)
                        if Full > 1:
                            Cache = Cache.replace(b"jpg\x00" + Hero, b"jpg\x00\x01\x00\x00\x00\x00", Full - 1)
                        EndTheCode = hex(len(Cache))
                        if len(EndTheCode) == 5:
                            EndTheCode = EndTheCode[3:5] + "0" + EndTheCode[2:3]
                        else:
                            EndTheCode = EndTheCode[4:6] + EndTheCode[2:4]
                        EndTheCode = bytes.fromhex(EndTheCode)
                        Cache = Cache.replace(Cache[0:2], EndTheCode, 1)
                Code = Code.replace(Id, Cache, 1)
                dieukienmod1=[]
                dieukienmod1.append(Cache)
                for dieukienmod2 in dieukienmod1:
                    if b"Hero" in dieukienmod2:
                         dieukienmod = dieukienmod2
                #print(Cache)
            file = open(File, "wb")
            W = file.write(Code)



            file.close()
            

    #======================================================AM_THANH_DATABIN=============================================================
    if b"Skin_Icon_SoundEffect" in dieukienmod or b"Skin_Icon_Dialogue" in dieukienmod:
        skin_id_input = IDMODSKIN
        sound_directory = Sound_Files
        sound_files = os.listdir(sound_directory)

        modsounddatabin(sound_directory)
        
    #=======================================================Skill_Databin============================================================        #========================================================DIEU_NHAY===========================================================
    file_path = file_mod_Modtion
    skin_id = IDMODSKIN
    all_ids = []

    for i in range(21):
        if i < 10:
            all_ids.append(skin_id[0:3] + "0" + str(i))
        else:
            all_ids.append(skin_id[0:3] + str(i))

    all_patterns = []

    for id in all_ids:
        hex_id = hex(int(id))[2:]
        all_patterns.append(bytes.fromhex(f"{hex_id[2:4]}{hex_id[0:2]}0000"))

    with open(file_path, "rb") as file:
        file_start = file.read(140)
        all_codes = []
        
        while True:
            segment_length = file.read(2)
            if segment_length == b"":
                file.close()
                break
            segment_length_value = segment_length[0] + segment_length[1] * 256 + 2
            code = segment_length + file.read(segment_length_value)
            if all_patterns[all_ids.index(skin_id)] in code:
                all_codes.append(code)
            elif all_patterns[0] in code:
                all_codes.append(code)

    dance_codes = []
    dance_codes_database = []
    dance_codes_mod = []

    for code in all_codes:
        if code[0:2] in b"6\x00S\x00":
            dance_codes_database.append(code)
        else:
            dance_codes.append(code)
            dance_codes_mod.append(code)

    dance_selection = 0

    if len(dance_codes_database) > 1:
        dance_selection = int(1)-1

    if len(dance_codes_database) > 0:
        selected_dance_code = dance_codes_database[dance_selection]
        dance_mod_id = selected_dance_code[21:25]
        for code in dance_codes:
            index = dance_codes.index(code)
            for pattern in all_patterns:
                position = code.find(pattern)
                if position != -1:
                    code_to_replace = code[position + 4:position + 8]
                    code = code.replace(code_to_replace, dance_mod_id, 1)
                else:
                    break
            dance_codes[index] = code
    else:
        for code in dance_codes:
            index = dance_codes.index(code)
            position_ref = code.find(all_patterns[all_ids.index(skin_id)])
            dance_mod_id = code[position_ref + 4:position_ref + 8]
            for pattern in all_patterns:
                position = code.find(pattern)
                if position != -1:
                    code_to_replace = code[position + 4:position + 8]
                    code = code.replace(code_to_replace, dance_mod_id, 1)
                else:
                    break
            dance_codes[index] = code

    with open(file_path, "rb") as file:
        content = file.read()
        file.close()

    for i in range(len(dance_codes_mod)):
        content = content.replace(dance_codes_mod[i], dance_codes[i], 1)

    if len(dance_codes) + len(dance_codes_database) == 0:
        for pattern in all_patterns:
            content = content.replace(pattern, b"00\x00\x00", 1)

    with open(file_path, "wb") as file:
        file.write(content)

    #===================================================VIEN================================================================
    if len(IDMODSKIN1) == 1:
        if b'Skin_Icon_HeadFrame' in dieukienmod:
            
            if chedovien == '1':
                data = dieukienmod
                target = b'\x00\x00\x10\x00\x00\x00Share_'+IDCHECK.encode()+b'.jpg'
                index = data.find(target) - 2
                two_bytes_before = data[index:index+2]
            if two_bytes_before != b'\x00\x00':
                if chedovien in ['1', '2']:

                    inp=file_mod_vien
                    with open(inp,'rb') as f:
                        ab=f.read()
                    a=two_bytes_before
                    i=ab.find(a)-4
                    vt=ab[i:i+4]
                    vtr=int.from_bytes(vt,byteorder='little')
                    vt1=ab[i:i+vtr]
                    id2='6500'
                    a1=bytes.fromhex(str(id2))
                    f.close()
                    i1=ab.find(a1)-4
                    vt11=ab[i1:i1+4]
                    vtr1=int.from_bytes(vt11,byteorder='little')
                    vt2=ab[i1:i1+vtr1]
                    vt1=vt1.replace(a,a1)
                    vt11=ab.replace(vt2,vt1)
                    with open(inp,'wb') as go:
                        go.write(vt11)
    #===================================================Skill_Ages================================================================
    CODE_BV_HERO = b''

    Files_Directory_Path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/'
    with zipfile.ZipFile('Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDMODSKIN[:3]}'+'_Actions.pkg.bytes') as File_Zip:
        File_Zip.extractall(Files_Directory_Path)
        File_Zip.close()
    HERO_NAME_LIST = os.listdir(Files_Directory_Path)
    for HERO_NAME_ITEM in HERO_NAME_LIST:
        NAME_HERO = HERO_NAME_ITEM
        directory_path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'
        giaima(sanitized_input)
        modages(directory_path)
        MKBV=b'\x36'
    if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod or IDCHECK == "53702":

        new_folder_path = Files_Directory_Path
        new_files_list = os.listdir(new_folder_path)
        NAME_HERO = new_files_list
        effect_name = NAME_HERO
        for new_file_item in new_files_list:
            effect_name = new_file_item
        for name1 in NAME_HERO:
            NAME_HERO = name1
#=========================================================NGOAI_HINH==========================================================
    INFO_MOD = f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/'
    with zipfile.ZipFile('Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDINFO[:3]}'+'_Infos.pkg.bytes') as f:
        f.extractall(INFO_MOD)
        f.close()
    
    đuongan=INFO_MOD+'Prefab_Hero/'+f'{NAME_HERO}'+'/'
    newpath=đuongan+'/'+NAME_HERO+'_actorinfo.bytes'
    giai(newpath)
    def skincanmod(data):
        trc1=r.find(timtrc,r.find(b'SkinPrefabG'))
        vt1=r.find(b'JTCom0',trc1-300)
        a1=r[vt1-31:]
        a3=vt1 - 31
        skin1=a1[:4]
        skin2=int.from_bytes(skin1,byteorder='little')
        data=r[a3:a3+skin2]
        #open('kb','wb').write(data)
        return data
    op = newpath


    trc=IDINFO
    with open(op,'rb') as f:
        r=f.read()
        r1=r
        timtrc = trc.encode()
        f.close()
    #skin
    mkcam=b''
    teninfobv1=NAME_HERO
    if IDCHECK == '14111':
        teninfobv1='141_DiaoChan'
    tenefec2=teninfobv1.encode()
    tenefec=teninfobv1.lower().encode()
    newteneffec=tenefec[4:].capitalize()
    newteneffec=tenefec[:4]+newteneffec
    str1 = b"hero_skill_effects/" + tenefec2 + b"/"
    str2 = b"hero_skill_effects/" + tenefec + b"/"
    str3 = b"Hero_Skill_Effects/" + tenefec2 + b"/"
    str4 = b"Hero_Skill_Effects/" + tenefec + b"/"
    str5 = b"hero_skill_effects/" + newteneffec + b"/"
    str7 = b"Hero_Skill_Effects/" + newteneffec + b"/"
    IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
    idnew=IDCHECK.encode()+b"/"
    mkcam =b''
    new1=b''
    new1+=skincanmod(r)
    if IDCHECK == '13311':
        if phukienv == "vangv":
            new1=ngoaihinhvaneovvang
            print('vanpkvang')
        if phukienv == "dov":
            new1=ngoaihinhvaneovdo
        if phukienv == '':
            new1=ngoaihinhvaneov
    if IDCHECK == '16707':
        new1=ngoaihinhkhieov
    if IDCHECK == '52007':
        if phukien == "do":
            new1=ngoaihinhdoveres
        if phukien == "xanh":
            new1=ngoaihinhxanhveres
    IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
    idnew=IDCHECK.encode()+b'/'
    ID1=IDCHECK.encode()
    if new1.find(b'prefab_skill_effects/hero_skill_effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
        FIND=new1.find(b'PreloadAnimatorEffects')-8
        VT1=new1[FIND:FIND+4]
        VTR=int.from_bytes(VT1,byteorder='little')
        VTM=new1[FIND:FIND+VTR]
        VTM9=VTM
        VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
        ELe=VTM.find(b'Element')-8
        ELe1=VTM.find(b'Element')-16
        VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
        DAU=VTM[ELe:ELe+4]
        VTR=int.from_bytes(DAU,byteorder='little')
        VTM1=VTM[ELe:ELe+VTR]#chuẩn
        VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
        VTCUOI=VTM[ELe:]#owr cuoois
        VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
        tinh=VTM.count(b'Element')
        VTM=VTCUOI
        KB=0
        CODEFULL=b''
        for i in range(tinh):
                ELe=VTM.find(b'Element')-8
                DAU=VTM[ELe:ELe+4]
                VTR=int.from_bytes(DAU,byteorder='little')
                VTM1=VTM[ELe:ELe+VTR]#chuẩn
                if VTM1.find(b'Vprefab_skill_effects/hero_skill_effects/') == -1:
                    CODEFULL+=VTM1
                    break
                VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                VTCUOI=VTM[VTR:]
                ELe1=VTM.find(b'Element')+7
                DAU1=VTM[ELe1:ELe1+4]
                VTR=int.from_bytes(DAU1,byteorder='little')
                VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                newvt=VTM1.find(b'Vprefab_skill_effects/')-8
                MOI=VTM1[newvt:newvt+4]
                VTR=int.from_bytes(MOI,byteorder='little')
                VTR3=VTM1[newvt:newvt+VTR]
                VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                VTM=VTCUOI
                CODEFULL+=CODE
        CODEFULL=CODEFULL.replace(str1,str1+ idnew).replace(str2,str2 + idnew)#.to_bytes(4,byteorder='little')
        CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
        new1=new1.replace(VTM9,CODEFULL)
        new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
        mkcam = b'\x05'#\x05
    if new1.find(b'Prefab_Skill_Effects/Hero_Skill_Effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
        FIND=new1.find(b'PreloadAnimatorEffects')-8
        VT1=new1[FIND:FIND+4]
        VTR=int.from_bytes(VT1,byteorder='little')
        VTM=new1[FIND:FIND+VTR]
        VTM9=VTM
        VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
        ELe=VTM.find(b'Element')-8
        ELe1=VTM.find(b'Element')-16
        VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
        DAU=VTM[ELe:ELe+4]
        VTR=int.from_bytes(DAU,byteorder='little')
        VTM1=VTM[ELe:ELe+VTR]#chuẩn
        VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
        VTCUOI=VTM[ELe:]#owr cuoois
        VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
        tinh=VTM.count(b'Element')
        VTM=VTCUOI
        KB=0
        CODEFULL=b''
        for i in range(tinh):
                ELe=VTM.find(b'Element')-8
                DAU=VTM[ELe:ELe+4]
                VTR=int.from_bytes(DAU,byteorder='little')
                VTM1=VTM[ELe:ELe+VTR]#chuẩn
                if VTM1.find(b'VPrefab_Skill_Effects/Hero_Skill_Effects/') == -1:
                    CODEFULL+=VTM1
                    break
                VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                VTCUOI=VTM[VTR:]
                ELe1=VTM.find(b'Element')+7
                DAU1=VTM[ELe1:ELe1+4]
                VTR=int.from_bytes(DAU1,byteorder='little')
                VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                newvt=VTM1.find(b'VPrefab_Skill_Effects/')-8
                MOI=VTM1[newvt:newvt+4]
                VTR=int.from_bytes(MOI,byteorder='little')
                VTR3=VTM1[newvt:newvt+VTR]
                VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                VTM=VTCUOI
                CODEFULL+=CODE
        CODEFULL=CODEFULL.replace(str3,str3 + idnew).replace(str4,str4 + idnew)#.to_bytes(4,byteorder='little')
        CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
        new1=new1.replace(VTM9,CODEFULL)
        new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
        mkcam = b'\x05'#\x05
    skinmoi=new1
    skinprefag=r.find(b'SkinPrefabG')-8
    tinhskinpre=r[skinprefag:skinprefag+4]
    tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
    tinhskinpre2=r[skinprefag:skinprefag+tinhskinpre1] #
    JTCom0 = tinhskinpre2.count(b"JTCom0")
    beginskin=tinhskinpre2[:101]
    CodeSkinNew=beginskin+new1*JTCom0 #
    tinhCodeSkinNew1=CodeSkinNew[:93]
    tinhCodeSkinNew=CodeSkinNew[93:]
    Elenmen=len(tinhCodeSkinNew).to_bytes(4,byteorder='little')+tinhCodeSkinNew[4:]
    SkinPrefag1=tinhCodeSkinNew1+Elenmen
    SkinPrefag=len(SkinPrefag1).to_bytes(4,byteorder='little')+SkinPrefag1[4:]
    codeskinnew=r1.replace(tinhskinpre2,SkinPrefag)

    def ArtSkinPrefabLOD(data3):
        a=skinmoi.find(b'\x00ArtSkinPrefabLOD')-7
        a10=skinmoi.find(b'\x00ArtSkinPrefabLOD')-3
        a3=skinmoi[a:a+8]
        a4=a3[4:]
        a2=skinmoi[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=skinmoi[a:a+vitri]
        a25=skinmoi[a10:a10+vitri2]
        a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD',b'\x00ArtPrefabLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data3=len(code).to_bytes(4,byteorder='little')+code[4:]
        return data3 
    def ArtSkinLobbyShowLOD(data4):
        a=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-7
        a10=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-3
        a3=skinmoi[a:a+8]
        a4=a3[4:]
        a2=skinmoi[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=skinmoi[a:a+vitri]
        a25=skinmoi[a10:a10+vitri2]
        a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyShowLOD',b'\x00ArtLobbyShowLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data4=len(code).to_bytes(4,byteorder='little')+code[4:]
        return data4
    #codeskinmd
    SkinMD=r[:skinprefag]

    #skinmd Art
    Art=SkinMD.find(b'ArtPrefabLOD')-8
    tinhskinpre=SkinMD[Art:Art+4]
    tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
    tinhskinpre2=SkinMD[Art:Art+tinhskinpre1] #
    #skinmd ArtLobbyShowLOD
    ArtLobby=SkinMD.find(b'ArtLobbyShowLOD')-8
    tinhArtLobby=SkinMD[ArtLobby:ArtLobby+4]
    tinhArtLobby1=int.from_bytes(tinhArtLobby,byteorder='little')
    tinhArtLobby2=SkinMD[ArtLobby:ArtLobby+tinhArtLobby1] #
    ArtSkinPrefab=b''
    ArtSkinPrefab+=ArtSkinPrefabLOD(skinmoi)
    CodeNewMD=SkinMD.replace(tinhskinpre2,ArtSkinPrefab)
    ArtSkinLobby=b''
    ArtSkinLobby+=ArtSkinLobbyShowLOD(skinmoi)
    CodeNewMD=CodeNewMD.replace(tinhArtLobby2,ArtSkinLobby)
    ArtLobbyIdle=CodeNewMD.find(b'ArtLobbyIdleShowLOD0')-8
    cammd=CodeNewMD[ArtLobbyIdle:999999]
    ArtLobbyIdleSkin=skinmoi.find(b'ArtSkinLobbyIdleShowLOD')-8
    camSkin=skinmoi[ArtLobbyIdleSkin:999999]
    camSkin=ArtSkinLobbyIdleShowLOD(camSkin)
    if mkcam == b'\x05':
        camSkin=camSkin.replace(CODEFULL,b'')
    CodeNewMD=CodeNewMD.replace(cammd,camSkin)
    CodeFull=codeskinnew.replace(SkinMD,CodeNewMD)
    RootDtrc=CodeFull[:84]
    RootDsau=CodeFull[84:]
    RootD1=RootDsau[8:12]
    VTR=int.from_bytes(RootD1,byteorder='little')#ArtPrefabLOD
    m=RootDsau.find(b'ArtPrefabLOD')-8
    CRE=b'c\x00\x00\x00\r\x00\x00\x00ActorNameJ\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1c\x00\x00\x00\x05\x00\x00\x00VFilesModBy_KunnAOV\x04\x00\x00\x00\x04\x00\x00\x00'
    tinhRootDsau=len(RootDsau).to_bytes(4,byteorder='little')+RootDsau[4:]
    tinhRootDtrc=RootDtrc+tinhRootDsau
    CodeDayDu=len(tinhRootDtrc).to_bytes(4,byteorder='little')+tinhRootDtrc[4:]
    CodeDayDu=CodeDayDu.replace(b"Light<",b"00000<")
    CodeDayDu=CodeDayDu.replace(b"imeline<",b"1234567<")
    CodeDayDu=CodeDayDu.replace(b"LOD3",b"LOD1")
    CodeDayDu=CodeDayDu.replace(b"LOD2",b"LOD1")
    tinhcam=CodeDayDu[:89]
    with open(op,'wb')as f: f.write(CodeDayDu)
    o=open(op,'rb')
    h=o.read(92)
    k=0
    while True:
        r1=o.read(4)
        if r1==b'':
            break
        KB=r1.hex()
        KB=KB[6:8]+KB[4:6]+KB[2:4]+KB[0:2]
        KB=int(KB,16)
        O=r1+o.read(KB-4)
        k+=1
    o.close()
    k=k.to_bytes(1,byteorder='little')
    tinhcam1=CodeDayDu[:88]+k
    CodeDayDu=CodeDayDu.replace(tinhcam,tinhcam1)
    with open(op,'wb')as f: f.write(CodeDayDu)


    if IDCHECK[:3] == '196':
        giai(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
        init()
        while True:
            Pathy = (f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
            try:
                break
            except:
                os.system("clear")
        IDSKINELSU = IDCHECK
        Light = "n"
        HD = "n"
        if len(IDSKINELSU) in (4,5):
            for FilePath in Pathy:
                path = Pathy + "/" + FilePath
                try:
                    file = open(path, "rb")
                    notfile = file.read(4)
                    file.close()
                    if notfile != b"PK\x03\x04":
                         
                         file = open(path, "rb")
                         Begin = file.read(92)
                         MD = []
                         MDD = []
                         
                         while True:
                             SL = file.read(4)
                             SL0 = SL.hex()
                             SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                             SL0 = int(SL0,16)
                             CodeZ = SL+file.read(SL0-4)
                             Find = CodeZ.find(b"SkinPrefabG")
                             if Find == -1:
                                 MD.append(CodeZ)
                             else:
                                 SkinPrefabG = CodeZ
                                 break

                         while True:
                             SL = file.read(4)
                             if SL == b"":
                                 break
                             SL0 = SL.hex()
                             SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                             SL0 = int(SL0,16)
                             CodeZ = SL+file.read(SL0-4)
                             MDD.append(CodeZ)
                
                         file.close()
                         
                         AllSkin = []
                         filez = open(".Cache","wb+")
                         Write = filez.write(SkinPrefabG)
                         filez.close()
                         filez = open(".Cache","rb")
                         BeginSkin = filez.read(101)
                         
                         while True:
                             SL = filez.read(4)
                             if SL == b"":
                                 break
                             SL0 = SL.hex()
                             SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                             SL0 = int(SL0,16)
                             CodeZ = SL+filez.read(SL0-4)
                             AllSkin.append(CodeZ)

                         filez.close()
            
                         for JTC in AllSkin:
                             tryFind = JTC.find(bytes(IDSKINELSU,"utf8"))
                             if tryFind != -1:
                                 ModSkin = JTC
                                 break
                         if tryFind == -1:
                             break                
                         filex = open(".Cache2","wb+")
                         Writein = filex.write(JTC)
                         filex.close()
                         filex = open(".Cache2","rb")
                         BeginSkinJTC = filex.read(96)
                         
                         SkinJTC = []
                         while True:
                             SL = filex.read(4)
                             if SL == b"":
                                 break
                             SL0 = SL.hex()
                             SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                             SL0 = int(SL0,16)
                             CodeZ = SL+filex.read(SL0-4)
                             SkinJTC.append(CodeZ)
                         KB = []
                         MD_S = MD + MDD

                         for i in range(len(SkinJTC)):
                             DK = 0
                             for k in range(len(MD_S)):
                                 if SkinJTC[i][8:25] == MD_S[k][8:25]:
                                     MD_S[k] = SkinJTC[i]
                                     DK = 1
                                     break
                             if DK == 0:
                                 KB.append(SkinJTC[i])
                                 
                         TT = []
                         for Name in KB:
                             if Name.find(b"_LOD") != -1:
                                 TT.append(Name)
                                 KB.remove(Name)
                         
                         for NameZ in KB:
                             if NameZ.find(b"LODEx0") != -1:
                                 TT.append(NameZ)
                                 KB.remove(NameZ)

                         for Name in KB:
                             if Name.find(b"_Show1\x04") != -1:
                                 TT.append(Name)
                                 KB.remove(Name)		
                         
                         for NameZ in KB:
                             if NameZ.find(b"LobbyIdle") != -1:
                                 TT.append(NameZ)
                                 KB.remove(NameZ)
                         
                         Eff_C = None
                         for Effects in KB:
                             if b"PreloadAnimatorEffects" in Effects and b"ffects/" in Effects:
                                 Eff_C = Effects
                                 break
                             
                         if Eff_C != None:
                             Find = -7
                             while True:
                                 Find = Eff_C.find(b"Element",Find+7)
                                 if Find == -1:
                                     break
                                 GT = Eff_C[Find-8]
                                 CodeC = Eff_C[Find-8:Find-8+GT]
                                 CodeCC = CodeC
                                 FIDSKINELSU = CodeC.find(bytes(IDSKINELSU[0:3]+"_", "utf"))
                                 FEIDSKINELSU = CodeC.find(b"/", FIDSKINELSU)
                                 NameHero = CodeC[FIDSKINELSU:FEIDSKINELSU]
                                 if len(IDSKINELSU) == 4:
                                     IDSKINELSUE = IDSKINELSU[0:3]+"0"+str(int(IDSKINELSU[3])-1)
                                 if len(IDSKINELSU) == 5:
                                     IDSKINELSUE = IDSKINELSU[0:3]+str(int(IDSKINELSU[3:5])-1)
                                 CodeC = CodeC.replace(NameHero, NameHero+b"/"+bytes(IDSKINELSUE,"utf"))
                                 GTS = bytes.fromhex(hex(GT+6)[2:4])
                                 CodeC = CodeC.replace(CodeC[0:1],GTS,1)
                                 GT2X = CodeC[0:15]+bytes.fromhex(hex(CodeC[15]+6)[2:4])+CodeC[16:]
                                 CodeC = CodeC.replace(CodeC[0:],GT2X,1)
                                 GTC = CodeC[55:61]+bytes.fromhex(hex(CodeC[61]+6)[2:4])
                                 CodeC = CodeC.replace(CodeC[55:62],GTC,1)
                                 Eff_C = Eff_C.replace(CodeCC,CodeC,1)
                                 
                             TSL = int(Eff_C.count(b"ffects/")/2)*6
                             GTBD = hex(Eff_C[0] + Eff_C[1]*256 + TSL)
                             GTBD = bytes.fromhex(GTBD[3:5]+"0"+GTBD[2])
                             Eff_C = Eff_C.replace(Eff_C[0:2],GTBD,1)
                             GTT2 = hex(Eff_C[82] + Eff_C[83]*256 + TSL)
                             GTT2 = bytes.fromhex(GTT2[3:5]+"0"+GTT2[2])
                             Eff_C = Eff_C.replace(Eff_C[82:84],GTT2,1)
                                 
                             KB.remove(Effects)                
                             
                             ModSkin = ModSkin.replace(Effects, Eff_C)

                             GT1 = str(hex(ModSkin[0]+ModSkin[1]*256+TSL))[2:6]
                             if len(GT1) == 3:
                                 GT1 = bytes.fromhex(GT1[1:3]+"0"+GT1[0])
                             if len(GT1) == 4:
                                 GT1 = bytes.fromhex(GT1[2:4]+GT1[0:2])
                             ModSkin = ModSkin.replace(ModSkin[0:2],GT1,1)
                                             
                             GT5 = hex(ModSkin[88]+ModSkin[89]*256+TSL)
                             if len(GT5) == 5:
                                 GT5 = bytes.fromhex(GT5[3:5]+"0"+GT5[2])
                             if len(GT5) == 6:
                                 GT5 = bytes.fromhex(GT5[4:6]+GT5[2:4])
                             GT5 += b"\x00"*2
                             ModSkin = ModSkin.replace(ModSkin[88:92],GT5,1)
                                     
            
                         for NR in range(len(TT)):
                             Cache = TT[NR]
                             Cache = Cache.replace(b"Skin",b"")
                             NC = len(Cache)
                             NC = str(hex(NC))
                             if len(NC) == 4:
                                 NC = NC[2:4]+"000000"
                                 NC = bytes.fromhex(NC)
                             else:
                                 NC = NC[3:5] + "0" + NC[2] + "0000"
                                 NC = bytes.fromhex(NC)
                             Cache = Cache.replace(Cache[0:4],NC)
                             NCK = int(Cache[4]) - 4
                             NCK = str(hex(NCK))
                             NCK = NCK[2:4]+"000000"
                             NCK = bytes.fromhex(NCK)
                             Cache = Cache.replace(Cache[4:8],NCK,1)
                             TT[NR] = Cache
                             
                             
                         for i in range(len(TT)):
                             for k in range(len(MD_S)):
                                 if TT[i][8:25] == MD_S[k][8:25]:
                                     MD_S[k] = TT[i]
                                     break
                         
                         JTCom0 = SkinPrefabG.count(b"JTCom0")
                         SkinPrefab = BeginSkin + ModSkin*JTCom0
                         Cache = SkinPrefab
                         NC = len(Cache)
                         NC0 = NC - 93
                         NC = str(hex(NC))
                         if len(NC) == 6:
                             NC = NC[4:6] + NC[2:4] + "0000"
                         if len(NC) == 7:
                             NC = NC[5:7] + NC[3:5] + "0" + NC[2] + "00"
                         NC = bytes.fromhex(NC)
                         Cache = Cache.replace(Cache[0:4],NC)
                         SkinPrefab = Cache
                         NCS = SkinPrefabG[93:97]
                         NC0 = str(hex(NC0))
                         NC0 = NC0[4:6] + NC0[2:4] + "0000"
                         NC0 = bytes.fromhex(NC0)
                         Cache = Cache.replace(NCS,NC0,1)
                         SkinPrefab = Cache

                         NCX = len(KB)
                         EndEvent = Begin
                         for A in range(len(MD)):
                             EndEvent += MD_S[A]
                         for B in KB:
                             EndEvent += B
                         EndEvent += SkinPrefab
                         for C in range(len(MDD)):
                             EndEvent += MD_S[C+len(MD)]
                         
                         if IDSKINELSU == "5443":
                             EndEvent = EndEvent.replace(MD[1],b"",1)
                             NCX -= 1
                             
                         NCZ = len(EndEvent)
                         NCZ0 = NCZ - 84
                         NCZ = hex(NCZ)
                         if len(NCZ) == 6:
                             NCZ = NCZ[4:6]+NCZ[2:4]+"0000"
                         if len(NCZ) == 7:
                             NCZ = NCZ[5:7]+NCZ[3:5]+"0"+NCZ[2]+"00"
                         NCZ = bytes.fromhex(NCZ)
                         EndEvent = EndEvent.replace(EndEvent[0:4],NCZ,1)
                         
                         NCV = EndEvent[84:88]
                         NCZ0 = hex(NCZ0)
                         if len(NCZ0) == 6:
                             NCZ0 = NCZ0[4:6]+NCZ0[2:4]+"0000"
                         if len(NCZ0) == 7:
                             NCZ0 = NCZ0[5:7]+NCZ0[3:5]+"0"+NCZ0[2]+"00"
                         NCZ0 = bytes.fromhex(NCZ0)
                         EndEvent = EndEvent.replace(EndEvent[0:4],NCZ,1)
                         EndEvent= EndEvent.replace(NCV, NCZ0, 1)
                         
                         XXX = EndEvent[88:92]
                         NCO = int(EndEvent[88])+NCX
                         NCO = hex(NCO)
                         NCO = NCO[2:4] + "000000"
                         NCO = bytes.fromhex(NCO)
                         EndEvent = EndEvent.replace(XXX,NCO,1)
                         
                         File = open(path,"wb")
                         WriteEnd = File.write(EndEvent)
                         File.close()
                         
                         os.remove(".Cache").remove(".Cache2")
                    else:
                         pass
                         file = file.close()
                except:
                    pass
        
        
    
    #=========================================================BIEN_VE==========================================================
    if b"Skin_Icon_BackToTown" in dieukienmod or b"Skin_Icon_Animation" in dieukienmod:
        RPL = CODE_BV_HERO
        cod = CODEBIENVE
        đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
        for ibv in range(1,2):
            with open (đuongan,'rb') as f : 
                bv = f.read()
                f.close()
            for kkbv in range(0,2):
                k1bv=k1bv+kkbv

            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(k1bv).encode()
            ab=ab.replace(b'coid',s1bv).replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+NAME_HERO.encode())
            if MKBV == b'\x36':
                dem1=0
                for i in RPL:
                    if i.find(b'<Action tag=""') !=-1:
                        break
                    dem1+=1
                VT=RPL[dem1+1:]#dem]
                VTR=b''.join(VT)
                VT1=VTR.count(b'<Condition id="')
                for i in range(VT1):
                    dem1=0
                    for i1 in VT:
                        if i1.find(b'<Condition id="') != -1 :
                            break
                        dem1+=1
                    VTR=VTR.replace(i1,b'')
                VTR=VTR.replace(b'  </Action>\r\n</Project>',b'')
                VTR+=b'  </Action>\r\n</Project>'
                codenew=cod.replace(b'  </Action>\r\n</Project>',VTR)
                codenew=codenew.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            else:
                cod=HPCAO+cod
                codenew=cod.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=bienve(codenew)
            aabv=b''
            aabv+=bienvecheck(codenew)
            CodeFullBV=aa
            ##printaa)
            #codenew=bv.replace(projack,codenew)
            codenew=bv.replace(projack,aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV).replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong', b'').replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi', b'').replace(b'strReturnCityFall', b'').replace(b'strReturnCityEffectPath', b'')
            if IDCHECK == '15412':
                codenew = codenew.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01',b'yenafixhuijidi')
                codenew = codenew.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01',b'yenafixhuicheng')
                codenew = codenew.replace(b'<String name="resourceName" value="yenafixhuicheng" refParamName="" useRefParam="true"/>',b'''</Event>
    </Track>
    <Track trackName="yenafix1" eventType="CheckSkillCombineConditionTick" guid="b588953f-80b3-4084-a5e2-6840b43b171c" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="bb954fcc-b78f-406a-bfb8-12c1bb2e3359">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="254999" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="216618f0-8c39-4789-903b-08ddecb68b45" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Condition id="32" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />
      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="96fa9d23-90bd-480b-af17-a12d8c342396">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Home2" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Condition id="32" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />
      <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="621e77cb-3dfc-40e3-8082-3e8603e3f7e2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Gohome2" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="yenafix1" eventType="TriggerParticleTick" guid="372cea2b-4677-4587-a037-9c13affdb97d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Condition id="32" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="007b4fc2-b841-493b-a390-91fde34a7624">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />
        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false" />
        <bool name="bForceIngoreCull" value="true" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huijidi_01_r" refParamName="" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="yenafix1" eventType="TriggerParticle" guid="3b9eb49a-febc-4403-827d-1dc93e40bf8b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Condition id="32" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="fba560da-156f-42fd-a4a0-b2d002e20c8b">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />
        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false" />
        <bool name="bForceIngoreCull" value="true" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huicheng_tongyong_01_r" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="yenafix1" eventType="TriggerParticle" guid="b4915550-8c39-430e-a71c-71fbf46dfaa4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_154_HuaMuLan" status="true"/>
      <Condition id="32" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="8.367" isDuration="true" guid="2f0136b1-53ec-45e3-b28b-ba244e737c6f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />
        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false" />
        <bool name="bForceIngoreCull" value="true" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/Huicheng_ personality_01 _r" refParamName="" useRefParam="false" />
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="bc9c6637-8bcd-4868-9025-ce5a4e01849a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="2" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="a0b63b54-8745-41f7-9423-fbc3805362bd">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huijidi_01" refParamName="" useRefParam="true" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="f7a7eaeb-083e-4558-bb2e-7d3799725089" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="2" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="e6c03e36-a18e-4ecd-b5fa-27824b611371">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huicheng_tongyong_01" refParamName="" useRefParam="true" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="cbb25ca6-00d8-48dd-8b94-57f5f36d4249" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="2" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="8.333" isDuration="true" guid="08b0db5c-b086-4656-abf8-3a80aebaddf2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/Huicheng_ personality_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />''')
            if IDCHECK == '13311':
                codenew = codenew.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/133_DiRenJie/13311/huijidi_01',b'Prefab_Skill_Effects/Component_Effects/13311/13311_5/Huijidi_01')
                codenew = codenew.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/133_DiRenJie/13311/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''Prefab_Skill_Effects/Component_Effects/13311/13311_5/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="664523ad-bc5e-4796-94a7-003b758fb8c4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="6" guid="KunnAOV_133_DiRenJie" status="true"/>
      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="ff3c2242-829b-4cfd-aaad-8e70a5e03ba2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="13311/Awaken/Home" refParamName="" useRefParam="false" />
        <int name="layer" value="2" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="972d1382-031a-4c10-8eeb-d10b3fc76f47" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="6" guid="KunnAOV_133_DiRenJie" status="true"/>
      <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="620b137f-72fa-4602-a653-72ae85944d33">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="13311/Awaken/Gohome" refParamName="" useRefParam="false" />
        <int name="layer" value="2" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '10620':
                codenew = codenew.replace(b'10620/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''10620/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_106_XiaoQiao" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="c534a92c-d326-4458-b877-a4e839aa475f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="45" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="Krixi" eventType="CheckSkillCombineConditionTick" guid="b24cf503-0ea8-4e2e-a6cf-704849c12624" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_106_XiaoQiao" status="true"/>
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="7ca4e3cb-7b14-4d89-ac98-a7f311ff2c76">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="106993" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="4" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="Krixi" eventType="PlayAnimDuration" guid="2997dd51-dcc7-40d4-a0ee-358f8cac2eb4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="b24cf503-0ea8-4e2e-a6cf-704849c12624" status="true" />
      <Condition id="4" guid="KunnAOV_106_XiaoQiao" status="true"/>
      <Event eventName="PlayAnimDuration" time="0.067" length="7.000" isDuration="true" guid="ef36d33a-fe2b-4ef5-9c60-01b0b8bbf435">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Home" refParamName="" useRefParam="false" />
        <int name="layer" value="2" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="Krixi" eventType="PlayAnimDuration" guid="24ce7fc1-71a9-426d-8c81-ea7d061d852d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="b24cf503-0ea8-4e2e-a6cf-704849c12624" status="true" />
      <Condition id="4" guid="KunnAOV_106_XiaoQiao" status="true"/>
      <Event eventName="PlayAnimDuration" time="0.067" length="7.000" isDuration="true" guid="faf68bfd-6c26-494e-a3ed-c20953edad0f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Idle" refParamName="" useRefParam="false" />
        <int name="layer" value="0" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '11607':
                codenew = codenew.replace(b'11607/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''11607/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="TriggerParticle1" eventType="TriggerParticle" guid="2172ad10-5ce9-47a4-aa56-cace6a30e3d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_116_JingKe" status="true"/>
      <Event eventName="TriggerParticle" time="7.000" isDuration="false" guid="1a1a92b3-ba06-4239-abc6-739be63c7747">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/116_jingke/11607/11607_huijidi_01" refParamName="" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />''')
            if IDCHECK == '11615':
                codenew = codenew.replace(b'11615/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''11615/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="6f3e1373-df06-4c20-8212-cf51c47a815c" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_116_JingKe" status="true"/>
      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="a5e127c4-4a08-48cf-bbf5-054c85b78aa8">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="buffId" value="116961" refParamName="" useRefParam="false" />
        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_116_JingKe" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="d62f8fb3-84f5-4c4a-9a27-b823160e32d1">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="180" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="99f9b620-fdb8-468a-8495-c9eef3083230" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="true" stopAfterLastEvent="true">
      <Condition id="4" guid="KunnAOV_116_JingKe" status="true"/>
      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="01de0da5-9334-4bc9-9e48-c378587071a6">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="SelfSkillCombineID_1" value="116961" refParamName="" useRefParam="false" />
        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '13015':
                codenew = codenew.replace(b'13015/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''13015/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_130_GongBenWuZang" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="0b9090b0-a50f-4a21-a836-d5fee4adaf3e">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="180" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="b781bec7-a0a4-47ea-b14f-22a5487ab7f6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_130_GongBenWuZang" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="6.850" isDuration="false" guid="d53624dd-ba5b-44a9-87e4-3636c5dc4ec1">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="80" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="eea8d318-4ccb-4e62-9d10-cb577f7b70b0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_130_GongBenWuZang" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="9734a1b5-629e-4fb4-b7c8-14fc329a9eba">
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/130_gongbenwuzang/13015/huicheng_tongyong_01_new" refParamName="" useRefParam="false" />
        <EulerAngle name="bindRotOffset" x="0.000" y="180.000" z="0.000" refParamName="" useRefParam="false" />
        <bool name="bReverseXWhenCameraMirror" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '13112':
                codenew = codenew.replace(b'13112/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''13112/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="a051af71-a5f2-4575-9071-7cfd947bb49e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_131_LiBai" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="10f7edf5-aea7-4d40-a466-426000b5ae41">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/131_libai/13112/Huicheng_tongyong_01_qipao" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bip001 Head" refParamName="" useRefParam="false" />
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />''')
            if IDCHECK == '13313':
                codenew = codenew.replace(b'13313/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''13313/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="cd9fc83b-cec9-4414-b884-00fe7c6c8e82" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_133_DiRenJie" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="8a15b50f-d8c7-4479-a6fb-ab20aa6aefae">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="180" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="bde6bebe-c0d6-4e96-821b-19f5cca00567" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_133_DiRenJie" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="a7090753-8b46-451c-ad4b-59df7b4b4304">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/133_direnjie/13313_Huicheng_01" refParamName="" useRefParam="false" />
        <bool name="bReverseRotOffsetWhenCameraMirro" value="false" refParamName="" useRefParam="false" />
        <bool name="bRevertZIn5v5" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '14110':
                codenew = codenew.replace(b'14110/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''14110/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveDuration0" eventType="SetActorNodeActiveDuration" guid="ffece0e5-414a-473c-978c-8c3977983b43" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_141_Diaochan" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="2a444000-9994-4392-b417-ca0714896eef">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="14108_piaodai_Mid" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveDuration0" eventType="SetActorNodeActiveDuration" guid="67036787-020e-4b54-a861-699ea8dde808" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_141_Diaochan" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="68f4f6b2-e830-4125-ae1f-cba787ea5b6c">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="Bip001/Ef_lxq_Bip001" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveDuration0" eventType="SetActorNodeActiveDuration" guid="3c26b3e2-4c10-456c-ba9d-0015cbf2f4a9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_141_Diaochan" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="9aca6ab6-0959-47b4-84bc-0cb9981d093d">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="Dummy001/Bone_Piao_R10/Bone_Piao_R11/Bone_Piao_R12/Bone_Piao_R13/Bone_Piao_R14/Ef_lxq_Bone_Piao_R14" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveDuration0" eventType="SetActorNodeActiveDuration" guid="9bcd3d32-5bad-4e09-8b92-72f6086beeba" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_141_Diaochan" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="b8f8581c-2be6-4ab7-88c0-f7a35cbedda5">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="Dummy002/Bone_Piao_L01/Bone_Piao_L02/Bone_Piao_L03/Bone_Piao_L04/Bone_Piao_L05/Ef_lxq_Bone_Piao_L05" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15710':
                codenew = codenew.replace(b'15710/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''15710/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2bd47bb6-ff11-4ec6-823d-3e64bb78393d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_157_BuZhiHuoWu" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.005" isDuration="false" guid="19186f55-ffcd-4095-b79a-34eeb624dab8">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="90" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="1b12d0e0-8e92-40e4-909a-72b21d52bcf5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_157_BuZhiHuoWu" status="true"/>
      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="ef567983-128d-4105-a2f5-ecc614a244dc">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Home" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="c1f6bece-4d4f-4bb8-9f5b-ec448a721456" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_157_BuZhiHuoWu" status="true"/>
      <Event eventName="PlayAnimDuration" time="7.000" length="4.500" isDuration="true" guid="a4f9646e-2cf2-4952-9cde-8d892eead301">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Gohome1" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="94206a84-71ae-4795-8ecd-728b8df2f93e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_157_BuZhiHuoWu" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="1037d202-d0de-4d35-b9d3-a4484a97c12e">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/157_buzhihuowu/15710/huicheng_tongyong_02" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bone_Qiu" refParamName="" useRefParam="false" />''')
            if IDCHECK == '16607':
                codenew = codenew.replace(b'16607/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''16607/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="46f2599d-9f70-41c0-8fed-0e9641d34002">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="170" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="ChangeHDHeightDuration0" eventType="ChangeHDHeightDuration" guid="991a6d57-99d0-4b7f-9214-fc9bd142dbcc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="ChangeHDHeightDuration" time="0.005" length="7.000" isDuration="true" guid="f2eae94a-c2de-4975-a43c-11ce8ae71e47">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="heightChange" value="1150" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="9b43034d-51e7-41f4-a63f-af1a531008ef" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="27fdbd06-2a6d-4443-b311-4642dfda5efe">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/166_yasewang/16607/T3_XiangYu_spell01_wuqi_A" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bip001 Prop1" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="8" eventType="SetActorNodeActiveDuration" guid="25e0d5fb-b0b7-4dde-b641-6f8256b6a5e2" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.100" length="6.900" isDuration="true" guid="47fb169e-8dbf-4f55-bfd9-d04e2120eaf6">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="1668_YaSeWang_wuqi_Mid" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="9" eventType="SetActorNodeActiveDuration" guid="89a9cec2-0638-4d63-bd66-17cca5d51ed4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="b92b5780-9ca2-4c0c-bdd1-d8327cf5ebbe">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="1668_YaSeWang_pifeng_Mid" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="9" eventType="SetActorNodeActiveDuration" guid="99803056-6cd8-4de6-87f3-fe9f965198f6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_166_YaSeWang" status="true"/>
      <Event eventName="SetActorNodeActiveDuration" time="0.000" length="7.000" isDuration="true" guid="08aa3438-b36e-4d70-9eb7-360ec244bc5a">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="1668_YaSeWang_pifeng_EF_Mid" refParamName="" useRefParam="false" />''')
            if IDCHECK == '17106':
                codenew = codenew.replace(b'17106/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''17106/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="CheckSkillCombineConditionDuration0" eventType="CheckSkillCombineConditionDuration" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="CheckSkillCombineConditionDuration" time="0.000" length="7.000" isDuration="true" guid="a86fc380-f146-4338-ab9d-9089461c7a43">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="171900" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="8d7d44fd-62fa-4b58-b473-9f603053239d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="bef7397c-8c43-4ebf-8430-e2fade278da6">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/ZhangFei_Huicheng_tongyong_02_Bone_Gu03" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bone_Gu03" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="63ea4315-cf17-43d1-8b83-663b4792168a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="62f2d14c-c209-441b-9087-c530e192af14">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/ZhangFei_Huicheng_tongyong_01" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="2c65e287-794f-41ea-80cc-d234b0ca3c4b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="96e2c4e7-52aa-4a63-81a8-9c06ad366695">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/ZhangFei_huijidi_01" refParamName="" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="9952cb48-8cb1-453d-8cf4-f4b0d943d083" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="false" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="0e3b89ab-f496-403b-bf75-c9896288c843">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/ZhangFei_Huicheng_tongyong_02" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="00f24da1-d7ae-45b4-906d-d29ef1ab0fba" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="false" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="56378a64-90b5-47d9-9fb1-86c10a2b0432">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/ZhangFei_huijidi_02" refParamName="" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2d201d5a-69bd-4061-986a-c9c63f7d1b79" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="false" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="8c545f4b-6f54-4013-b517-0e4807984e2d">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="180" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="cca59203-25b3-442e-b523-cf49cf26e810" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="b267c617-2f19-487c-b272-7cee49e7c2aa" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="981aecb3-b60e-4b9c-a057-2f08bf36df3a">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="300" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="StopTracks0" eventType="StopTracks" guid="00257a6b-f79e-4032-b768-b3a43bd13fba" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="StopTracks" time="7.000" isDuration="false" guid="9648785a-23f8-43b7-9a4d-b2e65619b0d2">
        <Array name="trackIds" refParamName="" useRefParam="false" type="TrackObject">
          <TrackObject id="1" guid="8d7d44fd-62fa-4b58-b473-9f603053239d" />
          <TrackObject id="2" guid="63ea4315-cf17-43d1-8b83-663b4792168a" />
          <TrackObject id="4" guid="9952cb48-8cb1-453d-8cf4-f4b0d943d083" />
        </Array>
      </Event>
    </Track>
    <Track trackName="PlayHeroSoundTick2" eventType="PlayHeroSoundTick" guid="23ad5e5e-7118-46d0-84de-0233863780d3" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="69" guid="b1697e33-b9f5-469f-9dce-4be52e867cf2" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="52cc4c9c-bf6a-4fe4-9792-d1d3d6e8be67">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="eventName" value="Play_Portal_M_ZhangFei_Skin6" refParamName="" useRefParam="false" />
        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />
        <bool name="canNotBeCulled" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="StopTrack0" eventType="StopTrack" guid="f69031af-ee5a-469c-a8a9-9a9a586ae872" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="69" guid="b1697e33-b9f5-469f-9dce-4be52e867cf2" status="true" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="964d19b5-6604-4447-bfee-ebf333001d15">
        <TrackObject name="trackId" id="74" guid="91f49296-8c45-4201-9485-4063f274f145" refParamName="" useRefParam="false" />
        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayHeroSoundTick2" eventType="PlayHeroSoundTick" guid="592aea6b-e117-4368-ad1c-cbaf4cac4de9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="69" guid="b1697e33-b9f5-469f-9dce-4be52e867cf2" status="false" />
      <Condition id="10" guid="KunnAOV_171_ZhangFei" status="true"/>
      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="bafb09ac-d407-4ed5-a9a4-06b9ae44feae">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="eventName" value="Play_Portal_ZhangFei_Skin6" refParamName="" useRefParam="false" />
        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />
        <bool name="canNotBeCulled" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '19605':
                codenew = codenew.replace(b'19605/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''19605/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="TriggerParticle2" eventType="TriggerParticle" guid="f20c5b77-0e1b-4f0d-9f83-4ad1495f6109" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="TriggerParticle" time="7.000" isDuration="false" guid="b2671c18-2139-4bee-bd51-fdc2074673f1">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/196_Elsu/19605/huijidi_19605" refParamName="" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />''')
            if IDCHECK == '19609':
                codenew = codenew.replace(b'19609/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''19609/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="b0cd80c6-3db7-4852-b25f-427378d1add1" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="6204d31c-4d24-4d4a-86a4-67e6abab88f2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="9d6bfcbc-92da-4e81-b70c-e650107855bd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="0.000" isDuration="false" guid="504568fa-71ae-4621-9583-99bf9affa91d">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Alpha_Mid" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="5d4970e5-fc18-4f27-a7cf-a3f03e321ae7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="true" execOnActionCompleted="true" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="7.000" isDuration="false" guid="cefd9183-aacf-4702-8979-911e2df21a26">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Alpha_Mid" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="daf7a160-2df6-4858-986b-2e23462dfc38" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="0.000" isDuration="false" guid="caf1a719-f165-4289-a11c-a6d1b47db969">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Mid" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="43477b51-47b4-499a-af13-e4edda4fd634" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="true" execOnActionCompleted="true" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="7.000" isDuration="false" guid="3d3b7dec-537a-4416-b566-630475659d51">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Mid" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="3129a955-84d6-4507-aa7e-d5af17996ab2" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="0.000" isDuration="false" guid="4f588695-621c-44a3-a4a7-378b4dc856fb">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Low" refParamName="" useRefParam="false" />
        <bool name="enabled" value="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetActorNodeActiveTick0" eventType="SetActorNodeActiveTick" guid="5403bb9a-e652-4014-a54a-779b3a63ebe2" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="true" execOnActionCompleted="true" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_196_Elsu" status="true"/>
      <Event eventName="SetActorNodeActiveTick" time="7.000" isDuration="false" guid="e7e4cea9-e342-41a0-9352-055930eaabb4">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="node" value="19610_BaiLiShouYue_Low" refParamName="" useRefParam="false" />''')
            if IDCHECK == '50604':
                codenew = codenew.replace(b'50604/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''50604/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_506_DarkKnight" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="929144cb-6fe8-42dd-975a-63b0f9c1b809">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="175" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle1" eventType="TriggerParticle" guid="2172ad10-5ce9-47a4-aa56-cace6a30e3d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_506_DarkKnight" status="true"/>
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="622a71fa-60a2-4084-aee4-61f55eef5d78">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/506_DarkKnight/50604/5065_Huicheng_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />''')
            if IDCHECK == '52007':
                codenew = codenew.replace(b'52007/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''52007/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="2a0028f3-08d2-4b85-9fa0-f3e68775f38e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="b6b26014-b2ac-4c88-8131-da4d3f0a61e1">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="buffId" value="520991" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="59e7e5f8-9826-44e1-ab86-c4ae7dd2b8d3" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="33ccc11f-c394-46ba-b398-3b39865f9a8d">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="buffId" value="520990" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="ChangeHDHeightDuration0" eventType="ChangeHDHeightDuration" guid="f092f299-98a7-4689-9c85-8c1ca8d1398b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="ChangeHDHeightDuration" time="0.000" length="7.000" isDuration="true" guid="df6460a1-5d0b-429b-af41-cefba824a685">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="heightChange" value="1600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="LeaveTriggerDuration0" eventType="LeaveTriggerDuration" guid="dc7695d3-c0bb-4598-8b2b-5a3e920b7373" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="LeaveTriggerDuration" time="0.000" length="7.000" isDuration="true" guid="e2c2bc0c-cd15-4383-a8e1-d010ada5b931">
        <TemplateObject name="TargetID" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="TargetSkillCombine_1" value="520991" refParamName="" useRefParam="false" />
        <int name="TargetSkillCombine_2" value="520990" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="47b35fd8-9333-41f5-81aa-be12e53aabfc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="9a110cf7-6cca-45e3-8f3a-271d23174426">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="150" refParamName="" useRefParam="false" />''')
            if IDCHECK == '52204':
                codenew = codenew.replace(b'52204/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''52204/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_522_Errol" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="442b6833-5044-41d8-8a8e-de66014ab5da">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="45" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="b781bec7-a0a4-47ea-b14f-22a5487ab7f6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_522_Errol" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="7.000" isDuration="false" guid="e8577fd4-d486-4d09-b64c-73a9b8800392">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="8266c0b2-3825-4f77-9cce-88d2a0421cbc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_522_Errol" status="true"/>
      <Event eventName="TriggerParticle" time="2.000" length="5.000" isDuration="true" guid="9d793a1c-e412-4f55-86bb-02a65a26e5a1">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/522_Errol/52204/Errol_Huicheng_L" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bip001 L Clavicle" refParamName="" useRefParam="false" />
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />
        <bool name="bUseRealScaling" value="true" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="32a7383d-8ed6-4bdf-b5fb-ec52debf94f4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_522_Errol" status="true"/>
      <Event eventName="TriggerParticle" time="2.000" length="5.000" isDuration="true" guid="bf89ad3b-98cf-4bc4-b136-378eb86b887a">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/522_Errol/52204/Errol_Huicheng_R" refParamName="" useRefParam="false" />
        <String name="bindPointName" value="Bip001 R Clavicle" refParamName="" useRefParam="false" />
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />
        <bool name="bUseRealScaling" value="true" refParamName="" useRefParam="false" />
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />
        <String name="customTagName" value="" refParamName="" useRefParam="false" />''')
            if IDCHECK == '53107':
                codenew = codenew.replace(b'53107/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''53107/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="0fb8c93a-4a62-4899-86b9-5b4cc7cbeeea" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_531_Keera" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="e4a68f01-7d90-4cfe-bbf0-0ec213e440a0">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="260" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="ChangeActorMeshDuration0" eventType="ChangeActorMeshDuration" guid="d4b0913b-f21c-4db0-8f75-8bd23963d58a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_531_Keera" status="true"/>
      <Event eventName="ChangeActorMeshDuration" time="0.000" length="7.000" isDuration="true" guid="1e9a19be-0476-4ba2-b47c-af25691e8465">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/531_Keera/53107/5318_Keera_S_LOD1" refParamName="" useRefParam="false" />
        <bool name="bUseOriginalActorMesh" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="8b6bcb1f-b143-4744-8965-72c68ed0da46" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_531_Keera" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="6.850" isDuration="false" guid="9fbd2c2e-962b-483d-8242-1b0fdef43dbb">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="80" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="f01bca9d-f9f5-49bc-a7e7-3d594966ce02" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_531_Keera" status="true"/>
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="e360d0de-3c33-411c-95b8-77fe60614a00">
        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />
        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/531_Keera/53107/53107_huijidi_01" refParamName="strReturnCityFall" useRefParam="false" />
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />
        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />
        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />
        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />''')
            if IDCHECK == '52011':
                codenew = codenew.replace(b'52011/huicheng_tongyong_01" refParamName="" useRefParam="true"/>',b'''52011/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="e952f97f-8631-454b-9cd9-eba3acb10660" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="130891af-3ab0-472d-baf7-cad62fe53ed6">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="buffId" value="520991" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3f2b173e-2fe3-4ea9-96c4-deb3276cc8cd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="d71f8ad5-9293-4222-8d88-b92d0241e9a5">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="buffId" value="520990" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="ChangeHDHeightDuration0" eventType="ChangeHDHeightDuration" guid="cd4b125f-cf39-4a33-b537-ca31e3e1a8e5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="ChangeHDHeightDuration" time="0.000" length="7.000" isDuration="true" guid="c8edf31f-003a-4115-a2f1-a3ccecb2f0f3">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="heightChange" value="1600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="4a296696-f4ba-459c-bff1-704798e88753" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="194bff4a-2ac2-42c4-889d-13433fd11d86">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="rotationY" value="90" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="CheckSkillCombineConditionTick0" eventType="CheckSkillCombineConditionTick" guid="99169b1a-e712-4076-814c-4577128a78de" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="e47f3714-60c4-4a67-82f2-256cd912f40f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="90005" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="CheckSkillCombineConditionTick0" eventType="CheckSkillCombineConditionTick" guid="862d574d-9c86-4f65-93f8-4d8a78590d8d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="2ea9fa8b-b335-4ec1-8f2d-341c89c8714a">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="90015" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="LeaveTriggerDuration0" eventType="LeaveTriggerDuration" guid="efd8dea4-1bd0-4e3b-86a5-cc4dcbe6dfd8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Condition id="4" guid="99169b1a-e712-4076-814c-4577128a78de" status="true" />
      <Condition id="5" guid="862d574d-9c86-4f65-93f8-4d8a78590d8d" status="true" />
      <Event eventName="LeaveTriggerDuration" time="0.000" length="7.000" isDuration="true" guid="5d866737-49f9-40e1-b570-1e4fca78d444">
        <TemplateObject name="TargetID" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="TargetSkillCombine_1" value="520991" refParamName="" useRefParam="false" />
        <int name="TargetSkillCombine_2" value="520990" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="9ff5a297-5c33-4581-abe2-f4c87c890e91" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="10" guid="KunnAOV_520_Veres" status="true"/>
      <Event eventName="SetAnimationParamsDuration" time="0.000" length="1.300" isDuration="true" guid="4312bb36-39f1-4112-9016-27a463d75d49">
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <Array name="boolNames" refParamName="" useRefParam="false" type="String">
          <String value="art_first" />
        </Array>
        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">
          <bool value="true" />
        </Array>''')
            with open (đuongan,'wb') as f : f.write(codenew)
            
            
            
            #Haste#
        RPL = CODE_BV_HERO
        cod = CODEBIENVE
        đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml'
        for ibv in range(1,2):
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1cechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            if IDCHECK == '11113':
                codenew = codenew.replace(b'''11113/JiaSu_tongyong_01" refParamName="" useRefParam="false" />''',b'''11113/JiaSu_tongyong_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="c606b328-f45f-4c98-98f0-a47bbf3cfdf1" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="KunnAOV_111_SunShangXiang" status="true"/>
      <Event eventName="SpawnBulletTick" time="0.000" isDuration="false" guid="1d78d4fc-9b19-494a-a7b8-4fc9af915d2f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="ActionName" value="Prefab_Characters/Prefab_Hero/111_SunShangXiang/skill/11113_Haste" refParamName="" useRefParam="false" />
        <bool name="bDeadRemove" value="true" refParamName="" useRefParam="false" />
        <int name="bulletUpperLimit" value="1" refParamName="" useRefParam="false" />
        <bool name="bAbort" value="true" refParamName="" useRefParam="false" />''')
            if IDCHECK == '16307':
                codenew = codenew.replace(b'16307/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''16307/juyoujing_jiasu_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '50112':
                codenew = codenew.replace(b'50112/JiaSu_tongyong_01',b'50112/suanni_sprint')
            if IDCHECK == '13116':
                codenew = codenew.replace(b'13116/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''13116/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15412':
                codenew = codenew.replace(b'15412/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15412/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '11607':
                codenew = codenew.replace(b'11607/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''11607/jingke_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '14111':
                codenew = codenew.replace(b'14111/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''14111/14111_luoer_Sprint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.200" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15009':
                codenew = codenew.replace(b'15009/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15009/T2_Spint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.150" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15015':
                codenew = codenew.replace(b'''15015/JiaSu_tongyong_01" refParamName="" useRefParam="false" />''',b'''15015/15015_HanXin_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="a9952930-5186-410d-a033-27bf3d518a32" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="20" guid="KunnAOV_150_HanXin" status="true"/>
      <Event eventName="SetAnimationParamsDuration" time="0.000" length="1.000" isDuration="true" guid="6eb33e50-720d-42f9-a730-77b7e0c95606">
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <Array name="boolNames" refParamName="" useRefParam="false" type="String">
          <String value="jiayuan" />
        </Array>
        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">
          <bool value="true" />
        </Array>''')
            if IDCHECK == '52011':
                codenew = codenew.replace(b'52011/JiaSu_tongyong_01',b'52011/520_Veres_long_sprint_loop')
            if IDCHECK == '54307':
                codenew = codenew.replace(b'54307/JiaSu_tongyong_01',b'54307/yao_sprint')
            with open (đuongan,'wb') as f : f.write(codenew)
            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml'
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1_leavecechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1_leave.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1_leave(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            if IDCHECK == '16307':
                codenew = codenew.replace(b'16307/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''16307/juyoujing_jiasu_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '50112':
                codenew = codenew.replace(b'50112/JiaSu_tongyong_01',b'50112/suanni_sprint')
            if IDCHECK == '13116':
                codenew = codenew.replace(b'13116/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''13116/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15412':
                codenew = codenew.replace(b'15412/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15412/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '11607':
                codenew = codenew.replace(b'11607/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''11607/jingke_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '14111':
                codenew = codenew.replace(b'14111/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''14111/14111_luoer_Sprint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.200" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15009':
                codenew = codenew.replace(b'15009/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15009/T2_Spint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.150" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15015':
                codenew = codenew.replace(b'''15015/JiaSu_tongyong_01" refParamName="" useRefParam="false" />''',b'''15015/15015_HanXin_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="a9952930-5186-410d-a033-27bf3d518a32" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="20" guid="KunnAOV_150_HanXin" status="true"/>
      <Event eventName="SetAnimationParamsDuration" time="0.000" length="1.000" isDuration="true" guid="6eb33e50-720d-42f9-a730-77b7e0c95606">
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <Array name="boolNames" refParamName="" useRefParam="false" type="String">
          <String value="jiayuan" />
        </Array>
        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">
          <bool value="true" />
        </Array>''')
            if IDCHECK == '52011':
                codenew = codenew.replace(b'52011/JiaSu_tongyong_01',b'52011/520_Veres_long_sprint_loop')
            if IDCHECK == '54307':
                codenew = codenew.replace(b'54307/JiaSu_tongyong_01',b'54307/yao_sprint')
            with open (đuongan,'wb') as f : f.write(codenew)
            
        đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE2.xml'
        for ibv in range(1,2):
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE2cechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            if IDCHECK == '16307':
                codenew = codenew.replace(b'16307/JiaSu_tongyong_01',b'16307/juyoujing_jiasu_01')
            if IDCHECK == '50112':
                codenew = codenew.replace(b'50112/JiaSu_tongyong_01',b'50112/suanni_sprint')
            if IDCHECK == '13116':
                codenew = codenew.replace(b'13116/JiaSu_tongyong_01',b'13116/huijidi_01_lobby')
            if IDCHECK == '15412':
                codenew = codenew.replace(b'15412/JiaSu_tongyong_01',b'15412/huijidi_01_lobby')
            if IDCHECK == '11607':
                codenew = codenew.replace(b'11607/JiaSu_tongyong_01',b'11607/jingke_sprint_01')
            if IDCHECK == '14111':
                codenew = codenew.replace(b'14111/JiaSu_tongyong_01',b'14111/14111_luoer_Sprint')
            if IDCHECK == '15009':
                codenew = codenew.replace(b'15009/JiaSu_tongyong_01',b'15009/T2_Spint')
            if IDCHECK == '15015':
                codenew = codenew.replace(b'''15015/JiaSu_tongyong_01" refParamName="" useRefParam="false" />''',b'''15015/15015_HanXin_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="a9952930-5186-410d-a033-27bf3d518a32" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="20" guid="KunnAOV_150_HanXin" status="true"/>
      <Event eventName="SetAnimationParamsDuration" time="0.000" length="1.000" isDuration="true" guid="6eb33e50-720d-42f9-a730-77b7e0c95606">
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <Array name="boolNames" refParamName="" useRefParam="false" type="String">
          <String value="jiayuan" />
        </Array>
        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">
          <bool value="true" />
        </Array>''')
            if IDCHECK == '52011':
                codenew = codenew.replace(b'52011/JiaSu_tongyong_01',b'52011/520_Veres_long_sprint_loop')
            if IDCHECK == '54307':
                codenew = codenew.replace(b'54307/JiaSu_tongyong_01',b'54307/yao_sprint')
            with open (đuongan,'wb') as f : f.write(codenew)
            
        đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE3.xml'
        for ibv in range(1,2):
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE3cechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            if IDCHECK == '16307':
                codenew = codenew.replace(b'16307/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''16307/juyoujing_jiasu_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '50112':
                codenew = codenew.replace(b'50112/JiaSu_tongyong_01',b'50112/suanni_sprint')
            if IDCHECK == '13116':
                codenew = codenew.replace(b'13116/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''13116/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15412':
                codenew = codenew.replace(b'15412/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15412/huijidi_01_lobby" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '11607':
                codenew = codenew.replace(b'11607/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''11607/jingke_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '14111':
                codenew = codenew.replace(b'14111/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''14111/14111_luoer_Sprint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.200" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="261208.020208" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15009':
                codenew = codenew.replace(b'15009/JiaSu_tongyong_01" refParamName="" useRefParam="false" />',b'''15009/T2_Spint" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="-0.150" z="0.000" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="check" eventType="CheckSkillCombineConditionTick" guid="639b3973-2cbf-4900-9bf6-a98b1306fc32" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="d97afbb6-9e4a-4349-8a31-ebf92f60320f">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />''')
            if IDCHECK == '15015':
                codenew = codenew.replace(b'''15015/JiaSu_tongyong_01" refParamName="" useRefParam="false" />''',b'''15015/15015_HanXin_sprint_01" refParamName="" useRefParam="false" />
        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="a9952930-5186-410d-a033-27bf3d518a32" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="20" guid="KunnAOV_150_HanXin" status="true"/>
      <Event eventName="SetAnimationParamsDuration" time="0.000" length="1.000" isDuration="true" guid="6eb33e50-720d-42f9-a730-77b7e0c95606">
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <Array name="boolNames" refParamName="" useRefParam="false" type="String">
          <String value="jiayuan" />
        </Array>
        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">
          <bool value="true" />
        </Array>''')
            if IDCHECK == '52011':
                codenew = codenew.replace(b'52011/JiaSu_tongyong_01',b'52011/520_Veres_long_sprint_loop')
            if IDCHECK == '54307':
                codenew = codenew.replace(b'54307/JiaSu_tongyong_01',b'54307/yao_sprint')
            with open (đuongan,'wb') as f : f.write(codenew)
            
            
        if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod:

            file_paths = [file_mod_skill1, file_mod_skill2]


            matching_files = []
            user_id = IDMODSKIN
            user_id_bytes = bytes(f"fects/{user_id[0:3]}_", "utf8")
            for file in file_paths:
                if user_id_bytes in open(file, "rb").read():
                    matching_files.append(file)
            for file in matching_files:
                if user_id == '13311':
                    with open(file, "rb") as f:
                        code_content = f.read()
                        code_content = code_content.replace(b"prefab_skill_effects/hero_skill_effects/133_direnjie/",
                                                              b"prefab_skill_effects/component_effects/13311/13311_5/")
                    with open(file, "wb") as f:
                        f.write(code_content)
                    break
                modified_codes = []
                buffer_codes = []
                with open(file, "rb") as f:
                    begin_content = f.read(140)
                    while True:
                        data_length = f.read(2)
                        if data_length == b"":
                             break
                        section_length = data_length[0] + data_length[1] * 256 + 2
                        code_section = data_length + f.read(section_length)
                        if user_id_bytes in code_section:
                             modified_codes.append(code_section)
                for code_section in modified_codes:
                    start_index = code_section.find(user_id_bytes) + 6
                    end_index = code_section.find(b"/", start_index) + 1
                    hero_name = code_section[start_index:end_index]
                    code_section = code_section.replace(b"Prefab_Skill_Effects/Hero_Skill_Effects",
                                                          b"prefab_skill_effects/hero_skill_effects")
                    code_section = code_section.replace(b"hero_skill_effects/" + hero_name,
                                                          b"hero_skill_effects/" + hero_name + bytes(user_id + "/", "utf"))
                    offset = code_section.find(b"prefab_skill_effects") - 4
                    length_change = bytes.fromhex(hex(code_section[offset] + len(user_id) + 1)[2:]) + b"\x00" * 3
                    code_section = code_section.replace(code_section[offset:offset + 4], length_change)
                    target_length = hex(len(code_section) - 4)[2:]
                    if len(target_length) == 3:
                        target_length = target_length[1:3] + "0" + target_length[0]
                    elif len(target_length) == 2:
                        target_length += "00"
                    target_length = bytes.fromhex(target_length)
                    code_section = code_section.replace(code_section[0:2], target_length, 1)
                    buffer_codes.append(code_section)
                modified_content = open(file, "rb").read()
                for index in range(len(modified_codes)):
                    modified_content = modified_content.replace(modified_codes[index], buffer_codes[index], 1)
                with open(file, "wb") as f:
                    f.write(modified_content)
                    
#=========================================================HIEU_UNG_VE_THAN==========================================================
    organSkin = "Resources/1.55.1/Databin/Client/Actor/organSkin.bytes"
    organSkin_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Actor/organSkin.bytes"
    shutil.copy(organSkin, organSkin_mod)
    giai(organSkin_mod)
    if IDCHECK in ("50108","14111","11107","15009","13015"):
        ID = IDCHECK
        file = open(organSkin_mod, "rb")
        IDN = str(hex(int(ID)))
        IDN = IDN[4:6] + IDN[2:4]
        IDN = bytes.fromhex(IDN)
        ALL_ID = []
        MD = int(ID[0:3] + "00")
        for IDNew in range(21):
            ALL_ID.append(str(MD))
            MD += 1
        ALL_ID.remove(ID)
        for x in range(20):
            IDK = str(hex(int(ALL_ID[x])))
            IDK = IDK[4:6] + IDK[2:4]
            IDK = bytes.fromhex(IDK)
            ALL_ID[x] = IDK
        Begin = file.read(140)
        Read = b"\x00"
        All = []
        while Read != b"":
            Read = file.read(36)
            if Read.find(IDN) != -1:
                All.append(Read)
            try:
                Max = Read[4] + (Read[5]*256)
                Max0 = str(hex(Max))
                if len(Max0) == 4:
                    Max0 = Max0[2:4] + "00"
                if len(Max0) == 5:
                    Max0 = Max0[3:5] + "0" + Max0[2]
                if len(Max0) == 6:
                    Max0 = Max0[4:6] + Max0[2:4]
                Max0 = bytes.fromhex(Max0)
            except:
                None
        file.close()
        file = open(organSkin_mod, "ab+")
        Read0 = file.read()
        for i in range(len(ALL_ID)):
            for j in range(len(All)):
                CT = All[j]
                if CT.find(IDN) != -1:
                    CT = CT.replace(IDN,ALL_ID[i])
                else:
                    CT = CT.replace(ALL_ID[i-1],ALL_ID[i])
                CTN = str(hex(Max0[0]+(Max0[1]*256)+1))
                if len(CTN) == 4:
                    CTN = CTN[2:4]
                if len(CTN) == 5:
                    CTN = CTN[3:5] + "0" + CTN[2]
                if len(CTN) == 6:
                    CTN = CTN[4:6] + CTN[2:4]
                CTN = bytes.fromhex(CTN)
                OZ = b" \x00\x00\x00"
                if len(CTN) == 1:
                    CT = CT.replace(OZ+CT[4:6],OZ+CTN+b"\x00",1)
                if len(CTN) == 2:
                    CT = CT.replace(OZ+CT[4:6],OZ+CTN,1)
                All[j] = CT
                XXX = file.write(CT)
                Max0 = CT[4:6]
        file.close()
        file = open(organSkin_mod, "rb")
        Read = file.read()
        Read = Read.replace(Begin[12:14],Max0,1)
        file.close()
        file = open(organSkin_mod, "wb")
        Z = file.write(Read)
        file.close()
        
        #print("Hiệu Ứng Vệ Thần")
    #=========================================================HABUANAK==========================================================
    if IDCHECK == "15009":
        đuongan1=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/BlueBuff.xml'
        đuongan2=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/RedBuff_Slow.xml'
        giai(đuongan1)
        giai(đuongan2)
        with open (đuongan1, 'rb') as f:
            noidung = f.read()
            noidung = noidung.replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick").replace(b'"skinId" value="15009"', b'"heroId" value="150"')
        with open (đuongan1,'wb') as f : f.write(noidung)
        with open (đuongan2, 'rb') as f:
            noidung = f.read()
            noidung = noidung.replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick").replace(b'"skinId" value="15009"', b'"heroId" value="150"')
        with open (đuongan2,'wb') as f : f.write(noidung)
        #=========================================================FIXLAG==========================================================
    if fixlag == 'y':
        if 1 == 1:
            if b"Skin_Icon_Skill" in dieukienmod or IDCHECK == "53702":
                shutil.copy(f'Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes', f'{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes')
                
                Pathy=f'{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes'
                pathasr=f'{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero'
                giaima(pathasr)
                bytes2xml(pathasr)
                modassetref(pathasr)
    try:
        nen(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod')
        folder_path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/'
        output_path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDCHECK[:3]}'+'_Actions.pkg.bytes'
        zip_folder(folder_path, output_path)
        shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/')
    except Exception as e:
        print(e)
        
    try:
        folder_path = f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/'
        output_path = f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDCHECK[:3]}'+'_Infos.pkg.bytes'
        zip_folder(folder_path, output_path)
        shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/')
        tinhskin0=tinhskin0 +1
        ats = int((tinhskin0/tinhskin)*100)
        print(colored(f"[✓] Quá trình: {ats}%","yellow"))
    except Exception as e:
        print(e)
đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'

path=os.path.join(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource')
Function_Track_Guid(path)
nen(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1')
try:    	
    folder_path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/'
    output_path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'
    zip_folder(folder_path, output_path)
except Exception as e:
    print(e)
else:
    pass
print(colored('Finishing...','green'))
xml2bytes(pathasr)
shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/')
print(colored('Done!','green'))