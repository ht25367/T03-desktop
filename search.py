import os
import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,file_name):
	df=pd.read_csv("./source.csv")
	source=list(df["name"])
	
	# 検索対象取得
	file_flg = os.path.isfile(file_name)
	# CSVﾌｧｲﾙが無い場合、
	if file_flg == False:
		if os.path.splitext(file_name)[1] != ".csv" :
			print("ファイル拡張子が正しくありません")
			return
		else:
			print(file_name + " ファイルがありません")
			file_flg = input("ファイルを作りますか？(y/n):")
			if file_flg == "y":
				# ファイル作成
				with open( file_name, "w" ,encoding="utf_8" ) as file:
					pass
			else:
				return
	

	# 検索
	if word == "" :
		eel.view_log_js("検索ワードが入力されていません。")
	elif word in source:
		eel.view_log_js("『{}』はあります".format(word))
	else:
		eel.view_log_js("『{}』はありません".format(word))
		# 追加
		add_flg=input("『{}』を追加登録しますか？(0:しない 1:する)　＞＞　".format(word))
		if add_flg=="1":
			source.append(word)
			print( word + " が追加されました")
		elif add_flg=="0":
			print(word + " は追加されませんでした")
		else:
			print("0 か 1 が入力されていません")
			print(word + " は追加されませんでした")

	# CSV書き込み
	df=pd.DataFrame(source,columns=["name"])
	df.to_csv("./" + file_name, encoding="utf_8-sig")
	print(file_name + "：", end="")
	print(source)
