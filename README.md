功能介紹
面部識別登入
程式在初次使用時建立一個個人的臉部模型，用來進行識別與登入。
程式引用了OpenCV模組，透過鏡頭對使用者面部採樣建立模型，在主程式
開啟時偵測並對比模型達到使用者登入的功能。
語音操控
使用者可以透過說出以下指令去達成基本操作：
● 新聞－播報透過爬蟲得到的新聞
● 英文新聞－播報英文翻譯過後的新聞
● 音樂－播放已存在資料庫中的音樂
● 直播－開啟一個Youtube新聞連播的直播
● 嗨－播報現在時間並打聲招呼
● 結束－結束辨識
程式引用SpeechRecognition、PyAudio、gTTs等模組組合達成以上功能。
手勢操控
使用者可以透過手比出以下動作去達成基本操作：（可對比語音操控）
● 1 － 播報透過爬蟲得到的新聞
● 2 － 播報英文翻譯過後的新聞
● 3 － 播放已存在資料庫中的音樂
● 4 － 開啟一個Youtube新聞連播的直播
● 5 － 播報現在時間並打聲招呼
● ok － 結束辨識
程式引用MediaPipe、OpenCV模組進行手勢識別與圖像識別達成操作。
新聞播報、直播
經過手勢或語音下達指令後執行，播報新聞上使用BeautifulSoup爬蟲ptt新
聞網主頁的新聞標題與網址，以random的方式選取一篇新聞寫入文字檔中，再
透過pyttx3模組讀出文字檔內容。
另一項播報新聞的功能，以開啟網頁視窗的方式執行，直接轉至新聞連播平
到播放新聞。
音樂播放
經過手勢或語音下達指令後執行，使用pygamea模組播放音樂，音樂以資
料夾的形式存放，每次下達播放指令時將會以隨機方式抽取一首歌播放。
打招呼時間播報
經過手勢或語音下達指令後執行，進行一個簡單的打招呼並播報幾月幾日
星期幾的資訊。
