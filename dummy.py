USE_DUMMY = True

DUMMY_SUMMARY = """**Multicast Communication**

* **Flooding-Based Multicasting**
	+ Each node sends a message M to its neighbors.
	+ Neighbors forward the message to their own neighbors, and so on.
	+ This process continues until all nodes receive the message.
* **Probability of Forwarding (Pf)**
	+ A parameter that determines the probability of a node forwarding a message to its neighbors.
	+ Example: If Pf = 0.01, then each node will forward the message to only 10% of its neighbors.
* **Connectivity Probability (Ps)**
	+ A parameter that determines the probability of a node being connected to other nodes in the network.
	+ Example: If Ps = 0.1, then each node is connected to 1000 other nodes.

**Hypercube-Based Multicasting**

* **4-Dimensional Hypercube**
	+ Each node has 4 dimensions (e.g., x, y, z, and w).
	+ Messages are forwarded along the dimensions of the hypercube.
	+ Example: Node 1001 sends a message to its neighbors in each dimension (x=0, y=1, z=0, w=1).

**Gossip-Based Data Dissemination**

* **Epidemic Behavior**
	+ A model that simulates the spread of information or rumors in a network.
	+ Three types of nodes: infected, susceptible, and removed.
	+ Infected nodes forward messages to their neighbors, while susceptible nodes receive messages from their neighbors.
	+ Removed nodes do not participate in message forwarding.

**Gossiping**

* **Push-Based Approach**
	+ Each node pushes a message to its neighbors.
	+ Example: Node 1001 sends a message to its neighbors in each dimension (x=0, y=1, z=0, w=1).
* **Pull-Based Approach**
	+ Each node pulls messages from its neighbors.
	+ Example: Node 0001 receives a message from Node 1001 and forwards it to its own neighbors.

**Side Effects of Gossip-Based Data Dissemination**

* **Difficulty in Deleting Messages**
	+ Once a message is spread, it can be difficult to delete or remove it from the network.
	+ Nodes that have already received the message may continue to forward it to their neighbors.
* **Use of Death Certificates**
	+ A mechanism to mark messages as "dead" and prevent them from being forwarded further.
	+ Death certificates are sent along with new messages to update nodes about the status of previous messages.

Note: The document has been restructured into sections and subheadings for easier reading. Some minor language corrections have also been made to improve clarity.

It seems like you've provided a comprehensive set of notes on distributed systems, specifically focusing on message-oriented communication. I'll summarize the key points for each section:

**Message-Oriented Communication**

* Message-oriented communication is an alternative to RPCs (Remote Procedure Calls) and remote object invocations.
* It's suitable when the receiving side may not be executing at the time a request is issued.
* Two types of message-oriented communication are:
	+ Transient: assumes that serious failures do not require automatic recovery.
	+ Persistent: provides intermediate-term storage capacity for messages.

**Message-Oriented Transient Communication**

* Many distributed systems and applications use the simple message-oriented model offered by the transport layer.
* Standard interfaces, such as Berkeley Sockets, have been introduced to make it easier to port an application to a different machine.
* The sockets interface is a low-level abstraction that provides a communication end point for sending and receiving messages.

**Message-Oriented Persistent Communication**

* Message-queuing systems provide extensive support for persistent asynchronous communication.
* They offer intermediate-term storage capacity for messages, without requiring either the sender or receiver to be active during message transmission.
* The basic idea is that applications communicate by inserting messages in specific queues.

**Multicast Communication**

* Multicast communication in distributed systems is the support for sending data to multiple receivers.
* Application-level multicasting techniques have been introduced, which rely on overlay networks to disseminate information.
* Two approaches are:
	+ Tree-based: nodes organize themselves into a tree structure, with a unique path between every pair of nodes.
	+ Mesh-based: nodes form a mesh network, where every node has multiple neighbors and there exist multiple paths between every pair of nodes.

**Gossip-Based Data Dissemination**

* Gossip-based data dissemination is an increasingly important technique for disseminating information in distributed systems.
* It relies on epidemic behavior, where nodes spread updates to their neighbors using local information.
* The main goal is to rapidly propagate information among a large collection of nodes using only local information.

**Stream-Oriented Communication**

* Stream-oriented communication supports the exchange of time-dependent information.
* DSes provide support for data streams, which are sequences of data units.
* A distinction is often made between different transmission modes:
	+ Asynchronous: no further timing constraints on when transmission of items should take place.
	+ Synchronous: a maximum end-to-end delay defined for each unit in a data stream.
	+ Isochronous: necessary that data units are transferred on time, with a maximum and minimum end-to-end delay.

I hope this summary helps! Let me know if you have any further questions or need clarification on any of these points.
"""
DUMMY_QUESTIONS = [
    '**Which method is more effective in disseminating information across a distributed system: a push-based approach or a pull-based approach? Justify your answer.**',
    '**Consider a network with limited connectivity. How would you balance the need for efficient message dissemination with the constraint of sparse connections? Provide a solution and explain your reasoning.**',
    '**Imagine a scenario where a critical message needs to be removed from circulation. What strategies could be employed to prevent further propagation, despite the presence of gossip-based data dissemination? Explain your approach.**',
    '**Compare the efficiency of tree-based and mesh-based multicast approaches in terms of resource utilization and latency. Provide a detailed analysis of their trade-offs.**',
    '**Suppose you are designing an epidemic behavior model for message dissemination. How would you incorporate features like difficulty in deleting messages, use of death certificates, or other strategies to mitigate potential issues? Justify your design decisions with logical reasoning.**'
]

DUMMY_TRANSCRIPT = """Oke, kita selesaikan dulu yang bagian communication ini ya. Nah, kita sampai di bagian multicast communication ya. Di situ kita sekarang sampai yang di bagian flooding base multicasting. Nah, di flooding base multicasting ini, ini mekanismenya jadi satu node ya, dia akan kirimkan pesan M di sini bilangnya ya ke neighbor-neighbornya. Kemudian pesannya ini mestinya oleh neighbornya akan kemudian diteruskan ke neighbor-neighbor yang lain. Itu caranya kemudian akhirnya semua node. Ya, akan mendapatkan pesan ini. Ya, itu yang floodingnya caranya begitu. Nah, ini mekanismenya itu misalnya node-nya itu Q ya, dia forwardkan message punya probabilitas itu kita bilang namanya P flood. Probability untuk apa namanya dari node-nya ini untuk menyebarkan pesan ini ke tetangga-tetangganya, neighbor-neighbornya. Nah, selain itu ada juga ya, parameter yang namanya pH ya, probabilitas satu node ini mempunyai, terhubung ya, terhubung atau terkoneksi dengan yang node-node yang lain. Ya, langsung aja pakai contoh ya. Jadi kalau misalnya ada satu jaringan terdiri dari banyak nodes, totalnya ada 10.000 node ini, ya kemudian pH-nya, probability S-nya 0,1, itu berarti masih, masing-masing node itu terkoneksi 0,1 kalau kita kalikan 10.000 kan berarti 1000 ya. Jadi masing-masing node itu terkoneksi dengan 1000 node yang lain. Ya, neighbor-nya jadi ada 1000 neighbor yang dia miliki untuk setiap node rata-rata. Ya, itu probabilitasnya seperti itu. Nah, kemudian berarti kan dia bisa ada kemungkinan dia akan nyebarkan ke neighbor-neighbornya ini ya, bisa sampai 1000 neighbor itu. Kemudian nanti, yang masing-masing neighbor yang terima pesan itu akan nyebarkan ke neighbor-neighbor yang lain, yang belum mendapatkan pesan itu tentu saja. Jadi kalau dia sudah pernah mendapatkan pesan itu, ya pesan itu nggak akan diteruskan. Ya, kemudian itu kita juga punya probability flat-nya itu 0,01, berarti kalau tadi dibilang setiap node itu punya, bentar ya, saya gunakan pointer mungkin supaya lebih jelas. Oke, jadi kalau setiap node-nya itu punya probabilitas terkoneksi dengan neighbor-neighbor node yang lain itu 0,1, berarti dia terkoneksi sampai 1000 node gitu ya. Nah, kalau P-flat-nya probabilitas dia untuk menyebarkannya itu 0,01, berarti dari 1000 node itu, dia nggak kirim ke 1000-nya ya, cuma ke 0,01 dari 1000 neighbor tersebut. Ya, jadi dengan demikian cuma 10. Ya, jadi cuma 10 neighbor yang dia kirimkan, kemudian nanti masing-masing neighbor-nya itu juga menggunakan setting probabilitas yang sama ya, jadi dia akan kirimkan ke 10 node yang lain lagi, 10 node lain. Misalnya contoh seperti itu ya, itu pun dengan yang jumlahnya cuma 10 tiap kali dikirim, 10 tiap kali dikirim ya, itu 5, ya mestinya tetap seluruh nodes itu, atau mayoritas dari node itu nantinya akan tetap terima pesan-pesan yang disampaikan itu. Dan jumlah pesan yang beredar ini, itu dibilangnya itu lebih, mestinya lebih nggak boros ya, 50 kali lebih nggak boros dibandingkan kalau kita melakukan full flooding, jadi masing-masing node kemudian sebar ke 1000, kemudian masing-masing 1000 itu akan kirimkan lagi ke yang lain ya. Itu kan bisa jadi, dia kirimkan, ke node-node yang sudah pernah dapat juga sebelum jadi, akhirnya itu wasted ya, boros. Ini kalau dengan yang cara begini, kita batasi dengan probabilitas gini, itu dari penelitian itu bisa pengurangnya sampai 50 kali, ya terjadi pengurangan ini lah, keborosan. Ya jadi bisa lebih hemat, tapi mencapai efektivitas yang sama. Di gambar di sini, itu juga bisa dilihat, kalau, PS nya berbeda-beda ya, PS kan berarti, koneksi antara satu node dengan neighbors nya itu seberapa banyak ya. Jadi kalau tadi contohnya 10.000 nodes totalnya, ya jadi kalau PS nya 0,2 berarti masing-masing node itu terkoneksi ke 2000 node yang lain. 0,4 terkoneksi ke 4000, kalau 0,6 berarti terkoneksi ke 6000 nodes yang lain gitu ya. Nah di sini juga bisa dilihat ya, apa namanya, kalau lihat grafiknya, PS yang 0,2 itu yang, ini ya yang paling bawah ya, kemudian 0,4 yang tengah, yang 0,6 yang paling atas. Jadi, dengan, probabilitas S nya ini semakin tinggi, tentu saja nantinya, jumlah nodes yang bisa dijangkau itu semakin banyak ya, semakin cepat juga akan mencapai, apa namanya, jumlah nodes yang akan mendapatkan pesan itu. Ya ini secara teoretis, pertama tengah, kalau pindah ke arah junior, mulai dari unit uni dengan unit nu bre, lalu atas PUS lagi,eternyai dari unit C denominant, jadi harusnya pinch 2. Kalau pindah ke awal,НumNo va ahorita dripping non-dividend, kalau puntual partition samaую, sehingga utih itu sangat banyak. Di awal berikut perangkangveniriness, ini classic set� Whoole Cancer, yang memang central 분위 ỡ di Amazon nya ya, ksat Éoter. Nah, Karena hypergip ini di contoh disini itu 4 dimensi. Ini kan juga totalnya ada 4 bit ya berarti ini 4 dimensi. Nah ini cara floodingnya itu dengan cara mengirimkan ke dimensi-dimensinya ini ya. Jadi ke 4 dimensi tersebut. Ini ada cara kerjanya penjelasannya bagaimana dilakukan dengan efisien. Jadi tidak boros ya pesannya. Bahkan ini bisa mengurangi pesannya itu tidak perlu dikirimkan sampai berulang ya. Ke node yang sama. Itu tidak mungkin terjadi. Karena ada pengaturan yang sangat baik kalau dalam hypergip ini. Kita coba lihat ya ilustrasi berikut ini. Jadi contoh ya kita punya hypergip seperti ini. Kemudian yang melakukan pengiriman pertama kali misalnya node 1001 ini. Dia akan flooding ke seluruh node yang lain. Kita lihat ada berapa langkah yang dibutuhkan sehingga bisa menjangkau seluruh node yang ada dalam hypergip. Jadi kita bisa lihat di sini. Jadi kita bisa lihat di sini. Nah tadi dibilang cara pengirimannya dikirim long dimension ya. Jadi sesuai dimensinya. Di sini kan ada 4 dimensi ya. Jadi 1001 akan mengirimkan ke 4 neighbor-nya. Jadi dia kirimkan neighbor ke 001 itu kalau dia sejalan dengan dimensi yang pertama ya. Yang paling kiri. Jadi. Kan dari 1001 dia akan terhubung. Ke 001 kalau kita ikutin yang dimensi pertama. Kalau ikuti yang dimensi kedua. Jadi yang bagian bit keduanya ini dia akan kirimkan ke neighbor 1101. Dimensi ketiganya 1011 dan terakhir yang 1000. Ini neighbor-nya itu terlihat di sini ya. Jadi dia kirim ke 001 yang dimensi pertama. Kemudian dimensi kedua ke bawah. Di sini. Dimensi yang ketiga itu dia ke depan. Kemudian dimensi empat yang dia ke kiri sini. Nah pada saat dia mengirimkan pesan ini. Dia kirimkan juga yang dimensinya. Jadi waktu kirim ke 001 pesan yang dikirimkan itu message-nya sendiri. Kemudian diikuti dengan dimensinya. Jadi dia kirimkan ke sini dengan dimensi pertama. Kemudian kirimkan ke 1101 M,2. Jadi dimensi kedua. Dan seterusnya. Karena kerjanya begini. Kenapa? Ini yang informasi yang kedua ini ya. 1, 2, 3, 4 dimensinya ini sangat penting. Sehingga itu nanti pengirimannya itu bisa beraturan. Kita coba ikuti lanjut ya. Jadi 0001 setelah menerima pesan dari 1001 ini. Dia akan meneruskan ke neighbor-nya. Nah caranya gini. Jadi karena dia melihat pesan yang dia terima itu M,1. Berarti. Yang pengirimnya itu sudah mengirimkan sejalan dengan dimensi pertama. Kalau dia misalnya kirimkan lagi ke yang berdi dimensi pertama. Dia akan balik ke sini. Karena dimensi pertama kan bagian ini ya. Yang pertama. Berarti akan balik ke sini. Jadi nggak perlu. Karena dia sudah dikirimkan M,1. Berarti dia sudah kirimkan ini di dimensi pertama. Ya dia jangan lakukan yang dimensi pertama lagi. Dia langsung lanjutkan. Jadi dia kirim ke dimensi pertama. Dimensi kedua, ketiga, keempat. Neighbor yang ada di dimensi kedua, ketiga, dan keempat. Jadi dari 0001. Dia akan kirimkan ke 0101, 0011, dan 0000. Ya sesuai dimensinya. Ya jadi yang di sini. Jadi dari sini ke bawah. Kemudian ke depan dan ke kiri. Ya. Sesuai dengan. Nah ini. Sekali lagi. Dia teruskan. Itu dengan informasi dimensinya ya. Jadi waktu kirim ke sini. M,2. Ini M,3. Ini M,4. Ya. Bagaimana dengan yang. Note 1101. Ini di sini ya dia. Nah dia karena dia terima M,2. Dia nggak mungkin. Nggak perlu kirimkan ke yang dimensi kedua lagi ya. Dan dia. Nggak perlu juga kirimkan ke dimensi yang pertama. Walaupun yang dimensi pertama kan sebelum. Kan ini kan. Cuma terkoneksi dengan yang dimensi kedua ya. Bagaimana dengan yang dimensi pertama. Nah yang dimensi pertama itu biarin yang diurus oleh note yang lain ya. Jadi instruksinya itu. Kalau dia terima M,2. Dia cukup teruskan ke neighbor. Yang dimensinya lebih tinggi dari 2. Jadi dia teruskan ke M,3 dan M,4. Itu ya. Jadi dia akan teruskan ke yang dimensi ke 3 dan 4. Dalam hal ini 1,1. Yang ini ya. 1111. Dan 11. 0,0. Bagaimana dengan yang 1011. Itu di sini. Karena dia terima M,3. Dia cuma teruskan ke. Ke dimensi yang keempatnya. M,4. Dalam hal ini yang 1010. Sini. Ya. Oke ini ya. Jadi ini. Yang. Lapisan pertama. Ya kemudian. Mereka teruskan ke neighbor. Ini yang neighbor-neighbor yang di lapisan kedua. Ya. Kita lanjutkan. Ini kan kan belum selesai semua ya. Karena. Masih ada beberapa yang belum terima pesan. Nah yang M,2 ini. Dari 0,1. 0,1. Karena dia 0,2 ya. Dia lanjutkan ke. Dimensi yang ke 3 dan ke 4. Ya. Jadi yang ke 3 ke sini. Yang ke 4 nya ke sana. Ya. Sementara kalau yang 0011. Itu berarti di sini. Ya. Dia sudah terima M,3. Jadi dia teruskan tinggal M,4 ke 0010. Ya. Terus lanjut yang 1111. Ini sini. Karena dia terima tadi M,3. Dia lanjutkan ke M,4 ke 1110. Ya. Sudah selesai. Ini yang lapisan ketiga. Dan yang terakhir lapisan ke 4. Itu tinggal satu aja yang belum ya. Ya ini yang akan lakukan yang 0111. Karena dia tadi terima M,3. Berarti belum selesai. Dia masih bisa teruskan ke M,4. Ya ke 01110. Itu cara kerjanya ya. Jadi. Maka ini bisa. Ini bisa awalnya bisa dari node mana pun ya. Untuk hypercube dengan 4 dimensi seperti ini. Itu berarti cuma dibutuhkan 4 langkah ya. Untuk bisa menjangkau semuanya. Mestinya dengan dengan ini kita bisa menarik kesimpulan ya. Kalau misalnya ini 5 dimensi. Ya berarti dia butuh 5 langkah. 6 dimensi dia butuh 6 langkah. Dan seterusnya. Ya. Oke. Bagaimana dengan struktur core. Ya. Struktur peer to peer lain yang kita sudah pelajari sebelumnya kan ini core ini ya. Bagaimana kalau mereka mau melakukan flooding. Ya. Apakah floodingnya juga bisa efisien ya. Jadi nggak perlu berulang ke banyak node ya. Kita coba lihat. Nah ini instruksinya bagaimana ini dilakukan flooding ya. Tapi saya untuk memudahkan menjelaskan saya gunakan sekali lagi ilustrasi ya. Oke. Kita punya core seperti ini. Untuk yang koneksi ke neighbor-neighbornya ini saya nggak perlu jelaskan kembali ya. Yang ini kan menggunakan kita bilangnya itu finger table ya. Jadi 1 node 1 dengan id 1. Dia terkoneksi ke yang i ke neighbornya yang plus 1 ya. Neighbornya yang plus 2 plus 4 plus 8 sampai plus 16 ya. Tapi ada beberapa yang. Mestinya arahnya itu ke node-node yang sama ya. Jadi makanya ini cuma misalnya 1 ini terkoneksinya yang ke 4, 9 dengan 18 ya. Dan 4 kemudian koneksi ke 9, 14 dan 20 dan seterusnya. Ya. Yang itu saya nggak perlu jelaskan ulang. Tolong dilihat kembali yang slide-slide yang sebelumnya ya. Penjelasan tentang core. Oke. Untuk yang ini contoh ini. Misal. Kita mulai dari yang node 9. Ya. Node 9 akan melakukan flooding pengiriman pesan ya ke semua node-node yang lain. Bagaimana ini dilakukan? Nah. Node 9 ini. Dia di dalam finger table-nya dia bisa melihat dia punya koneksi ke neighbor yang 11, 14, 18 ya. Dan terakhir 28. Jadi ada 4 neighbor ya. 11, 14, 18 dan 28. Nah. Dia kirim ke 4-4 ini ya. 11, 14, 18 dan 28. Nah. Waktu mengirimkan pesan itu dia juga menyatakan ya. Contoh ya. Yang dia kirimkan ke 11, 14, 18. Nah. Yang waktu dia kirimkan ke 11. Dia kirimkan pesannya kemudian diikuti dengan pemberitahuan. Oke. 11 kamu dapat pesan. Nah. Tolong teruskan pesan ini. Ke node-node neighbormu yang ada dalam range 11, 14 ya. Rangenya ini yang 11-nya yang kita bilangnya ini kan pipenya tertutup ya. Kalau yang 14-nya pipenya terbuka. Jadi kalau yang ini kan berarti ke node-node yang lebih besar sama dengan 11. Tapi lebih kecil dari 14 ya. Jadi ya 11, 12, 13 gitu ya. Pipe ini artinya. Nah. Jadi 11 ini. Waktu dia terima pesan. Dia ditugaskan juga untuk meneruskannya ke node-node yang ada dalam area ini. 11 sampai kurang dari 14 ya. Sementara kalau yang 14 diberitahu kamu teruskan 14 sampai 18. Ya. Jadi 11, 14, 18, 28 ini. Node 9 ini itu melakukan pembagian tugas gitu ya. Selain ngirimkan pesan M. Dia juga memberikan pembagian tugas ya. Jadi yang 11. 11 sampai 14. Sementara yang 14. Tugasnya dari 14 sampai 18. 18 tugasnya 18 sampai 28. Sedangkan 28 itu sisanya. 28 sampai balik lagi ke 9. Ya. Jadi masing-masing punya tugas itu. Punya area masing-masing. Jadi nggak akan bentrok. Ya. Oke. Kemudian kita lanjutkan. Ini lapisan pertama. Ya. Step pertama. Ya. Kemudian yang 11. Dia akan ditugaskan untuk sebelah. Ya. 11 sampai 14. Ya. Karena dia melihat. Neighbour-nya dia. Dia koneksi ke 14, 18, 20 dan seterusnya gitu ya. Nah. Antara 11 dengan yang 14. Dia kan. Diminta. Ditugaskan untuk mengirimkan. Kirimkan sampai kurang dari 14. Jadi 14 mestinya nggak termasuk ya. Jadi harus yang lebih kecil dari 14. Sementara dia nggak punya neighbour lain yang lebih kecil dari 14 ya. Jadi 12 dan 13 itu nggak ada. Neighbour-nya. Jadi 11 ini nggak akan meneruskan ke manapun. Jadi pesannya berhenti di dia. Dan dia kemudian nggak meneruskan ke node manapun. Karena tidak ada. Ya. Sementara 14. Sama kondisinya. Karena 14 dia terkoneksi pertama ke 18 ya. Kemudian yang lain-lain sudah lebih besar dari 18 ya. Jadi antara 14 sampai 18 nggak ada node-node yang lain. Jadi 14 juga. Tidak meneruskan pesannya. Bagaimana dengan 18? Nah 18 ini. Dia terkoneksi dengan 20, 28 dan seterusnya. Karena dia tugasnya itu 18 sampai 28. Ya dia akan teruskan ke yang 20. Sementara 28 itu di luar jangkauannya. Jadi dia akan teruskan ke node 20. Ya. Nah kemudian yang node 20 itu pada saat 18 memberikan pesan itu. Dia juga diberitahu. Kamu teruskan ini ke node-node yang berada di 20 sampai 28. Sampai kurang dari 28. Ya. Ini sudah yang kedua ya. Yang 28. Ya sebenarnya 28 nanti dia akan teruskan juga. Jadi yang ini yang dari 18 ke 20 ya. Mungkin kita tinggalkan dulu. Kita coba teruskan dulu yang 28 ya. 28 ini terkoneksi ke 1 kemudian 4. Kemudian sebelum. Ini 14 ya. 1, 4 dan kemudian ke. 14. Karena dia ditugaskan ke 28 sampai 9. Ya. Jadi dia akan dikirimkan ke 1, 4. Dan selesai ya. 1 dan 4 ya. Karena yang ini kan sudah 14 ya. Jadi sudah di atasnya 9 ya. Jadi cuma 1 dan 4. Jadi dia akan teruskan ke 1 dan 4. Dengan memberikan instruksi lanjutkan gitu ya. Jadi ke 1 ya. 1, 4. Yang 4 nya 4, 9. Ya. Ini jadi di lapisan kedua ya. Di langkah kedua. Pesannya itu menjangkau node 20, 1 dan 4. Ya. Kemudian kita lanjut. Yang dari 1 nanti akan coba teruskan. 4 coba teruskan. Yang 20 juga akan coba teruskan. Yang 20 tadi terima pesan dia diminta teruskan 20 sampai 28 ya. Nah dia terkoneksi cuma ke 21. Kemudian sudah langsung 28. Jadi dia akan teruskan ke yang 21 ini. Kemudian 21 diminta teruskan 21 sampai 28. Ya. Sementara kalau yang dari 1 dia terkoneksi ke 4. Ya karena dia ditugaskan 1 sampai 4. Berarti sudah gak ada yang perlu dikirimkan ya. Bagaimana dengan 4? 4 sampai 9 ya dia sudah gak ada. Karena neighbor nya yang terdekat 9 ya. Sementara 9 mestinya gak perlu dikirimkan lagi. Ya. Jadi selesai. Jadi yang di step ketiga yang dijangkau cuma 21 ya. Ya. Setelah itu selesai ya. Semua sudah terjangkau ya. Jadi 21 pun kalau diminta untuk meneruskan ya. Dia terkoneksi pertama ke neighbor yang 28 ya. Jadi antara 21 sampai 28 gak ada neighbor lain. Jadi dia gak bisa teruskan. Jadi bahkan untuk yang di kasus ini cuma 3 step yang dibutuhkan. Ya. Tapi nanti kalau misalnya susunannya beda. Note-note yang ada mungkin lebih banyak ya. Bisa jadi jumlah step yang dibutuhkan akan lebih banyak juga. Ya. Nah mestinya kalau disini totalnya ada 32 atau ini 2 pangkat 5 ya. Ini mestinya maksimum langkah yang dibutuhkan juga hanya 5 step ya. Kalau misalnya totalnya 64 ya total yang dibutuhkan mestinya ya juga 6 step ya. Sesuai dengan ini ya log n nya. Ya log n dasar 2 nya. Oke. Oke ini cara kerjanya yang core. Nah lanjut teknik lain selain flooding ada juga yang namanya gossip based data dissemination ya. Nah yang teknik gossip based ini sebenarnya bagian dari satu teknik yang kita bilangnya itu epidemic behavior. Jadi epidemic kita tahu epidemic itu bicara tentang penyebaran penyakit yang menular ya infectious diseases. Sama seperti yang apa namanya kondisi yang menular. Apa namanya kondisi yang barusan kita lewati waktu pandemi lalu ya. Itu kan epidemic dinyatakan sebagai kasus epidemic bahkan dianggap sebagai pandemic ya. Jadi kalau epidemic itu biasanya area nya lebih kecil terbatas. Tapi kalau sudah dinyatakan pandemic itu berarti area nya itu sampai ke seluruh dunia ya. Jadi bahkan lebih lebih parah gitu ya kalau kalau kasus namanya pandemic. Nah yang ini epidemic behavior sebenarnya belajar dari kondisi bagaimana. Penyakit ini penyakit menular ini disebarkan ya. Bagaimana mengirimkan pesan menyebarkan pesan ini ke banyak node dengan dengan dengan behavior nya itu seperti penyakit menular ini menyebar dari satu orang ke orang orang yang lain. Ya jadi dalam dalam konsep epidemic epidemic behavior ini ada tiga. Ada tiga kategori atau tiga kelas ya dari dari node node nya itu. Jadi ada node node yang kita bilang kasus statusnya itu infected. Berarti node tersebut memiliki penyakit dalam hal ini penyakitnya itu memiliki pesan ya pesan yang kemudian dia karena dia terinfeksi dengan pesan ini ya dengan message ini. Ya dia kemudian akan menyebarkan pesan ini ke node node tetangganya ya. Nah node node yang. Belum mendapatkan pesan ini atau dengan kata lain node node yang belum terinfeksi dengan pesan pesan ini kita bilang sebagai node node yang susceptible. Ya. Ini yang status kedua ya kategori atau kelas kedua ya. Jadi ada yang infected mendapatkan pesan. Kemudian ada yang belum mendapatkan pesan yang kita bilang namanya susceptible. Dan kemudian yang status terakhir atau kelas yang terakhir itu yang kondisinya remove. Jadi yang remove ini. Node node yang. Mendapatkan pesan infected ya tapi dia tidak tidak not willing ya jadi dia tidak mau menyebarkan pesan itu lebih lanjut. Ya jadi makanya dia kondisinya remove. Ya kondisinya dia nggak mau terlibat ya jadi nggak ikut menyebarkan penyakit atau menyebarkan message ini. Ya ini ini di algoritma yang epidemic behavior ini kita punya. Tiga kemungkinan. Kelas seperti ini ya infected susceptible sama yang remove ya. Nah lanjut. Saat data ini disebarkan message ini disebarkan. Tiap message itu punya timestamp atau ada versinya ya tujuannya untuk membedakan antara satu pesan dengan pesan yang lain. Ya jadikan pesan ini kan disebarkan bisa jadi kemudian ada pesan lain yang juga kemudian disebarkan. Nah bagaimana kita tahu. Pesan yang pertama ini dengan yang pesan yang kedua itu bukan pesan yang sama. Ya nah untuk membedakan itu makanya pesan pesannya itu bisa diberi timestamp atau diberikan versi ya ini pesan yang versi pertama ini pesan versi kedua ya. Atau diberikan timestamp tadi ya jadi karena perbedaan yang ini time pesan ini di generate. Pada pada timestamp sekian gitu ya. Beneran yang yang message pesan kedua nanti bisa dilihat. Apakah dia di generate pada timestamp. Apakah dia di generate pada waktu yang sama atau waktu yang lebih belakangan ya. Dengan demikian kita bisa tahu yang ini sama atau beda dengan pesan yang sebelumnya. Ya itu tujuannya memberikan timestamp atau memberikan versi ya. Kemudian model propagasi yang cukup populer di gossip base atau di epidemic behavior ini adalah yang anti entropi kita bilangnya. Ya di anti entropi itu ada tiga kemungkinan. Artian② Post狀장 Note yang lain itu note-note yang susceptible Note-note yang belum mendapatkan pesan Itu skin error pertama Jadi dia mekanismenya itu cuma push Dari yang infected Mudah-mudahan Diterima oleh note-note yang susceptible Bisa jadi pada saat dia push message ini Dia push ke message ke note lain Yang note ini ternyata sudah infected Maksudnya dia sudah terima pesan ini Ada kemungkinan seperti itu Nanti kita lihat Di skenario ini Apakah skenario ini cukup efektif Kalau kita cuma mekanismenya itu push Yang skenario kedua Itu mekanismenya itu pull Jadi note yang Sekarang kalau ini melakukan pull Note ini berarti note yang susceptible Dia belum mendapatkan pesan Dia belum infected Dia masih susceptible Jadi belum mendapatkan pesan apapun Nah dia Pull Menarik dari tetangganya Apakah ada pesan yang baru Yang saya perlu terima Jadi dia pull Update Apakah ada pesan baru Misalnya dari note lain yang Queue Bisa jadi Note yang tetangganya itu Note-note yang susceptible juga Jadi kalau dia susceptible Berarti ya tidak ada pesan baru Karena sama-sama Tidak mendapatkan message Atau mendapatkan penyakit itu Tapi Kalau dia misalnya pull itu dari Note yang infected Ya dia akan mendapatkan Pesan yang baru Itu skenario kedua Jadi pertama push Yang kedua itu dengan Skenario pull Dan yang ketiga itu Kombinasi keduanya Push dan pull approach Ya Nah dari penelitian Kalau kita gunakan skenario ini cuma push Ya Itu ternyata Kurang efektif Ya Terutama ini kalau Kondisinya itu sudah Banyak note-nya yang terinfeksi Karena sudah banyak note-nya yang infected Jadi Untuk setiap note itu Bisa menemukan Note baru Dimana dia mau push kan ya Dia push Message ini ke note lain Kemungkinan note lain ini Note yang susceptible yang belum mendapatkan Message Itu kemungkinannya kecil Sehingga bisa jadi Pada saat sudah terlalu banyak note yang infected Itu Naiknya sedikit ya Jadi sudah Sudah terlalu susah untuk mencari Note-note yang susceptible Jadi kurang efektif Modelnya kalau kita gunakan skenario Push Ini terutama sekali lagi Kalau Kalau Sudah terlalu Terlalu banyak note yang infected Ya Sebaliknya kalau kita gunakan yang skenario pull base itu Ternyata Baik ya hasilnya itu lebih baik daripada yang Skenario pertama Ya Terutama juga kalau misalnya kondisinya Banyak note yang sudah terinfeksi Karena mekanismenya itu pull berarti yang lakukan pull itu sebenarnya mereka yang susceptible jadi yang belum kena Nah kalau ada banyak neighbor-neighbornya yang infected Kemungkinan dia akan terinfeksi yang susceptible ke kemungkinan terinfeksi akan sangat sangat besar Ya jadi pada saat Apa namanya pesan-pesannya ini sudah tersebar banyak ada many notes yang Infected Yang susceptible notes pun masih akan mendapatkan update Ya itu itu yang keuntungan dari menggunakan yang model pull base ini Ya Secara overall dibilang Strategi yang kombinasi keduanya push dan pull itu Dirasa lebih baik dibandingkan yang Push only ataupun yang pull base Ya Oke Nah varian dari yang epidemic Behavior ini yang kita bilang sebagai Gossiping atau rumor spreading Ya ini bicara tentang gossip based data dissemination Ya Cara kerjanya seperti ini jadi itu Kalau yang ini Ya Secara dasarnya sama sama dengan yang tadi yang di epidemic tadi ya Jadi setiap note itu dia akan Coba push kalau disini yang coba dilihat cuma yang skenario push ya Dia akan coba push update Ke note yang lain ya ini gossip Jadi sama ya epidemic ini makanya dibilang namanya juga Gossiping ini variannya dari yang epidemic Kalau yang gossiping sama ya jadi kalau kita mendapatkan rumor Atau pesannya itu jadi disebut sebagai rumor Nah rumornya ini kemudian disebarkan ke tetangga-tetangga yang lain ya Menggossip ya menggossip tentang rumor ini ya dengan tetangga yang lain ya Harapannya tetangga yang lain kemudian akan mendapatkan rumor ini kemudian akan Nyebarkan lagi rumornya ke tetangga-tetangga yang lain ya Ini yang mekanisme gossiping seperti ini Nah disini Di ilustrasi ini kita juga bisa menggunakan Variable yang probability ya probability stock Jadi ini kemungkinan Kemungkinan satu note ya Untuk menjadi remove Masih ingat ya tadi kan ada tiga status ya Infected, susceptible, sama yang remove Jadi probabilitas Note yang infected itu menjadi remove itu probabilitasnya kita bilang yang P stop ini Jadi dia stop untuk menyebarkan rumor ya Dia tidak mau lagi menyebarkan rumor Dia mendapatkan rumor tapi dia tidak menyebarkan atau meneruskan ke tetangga-tetangga yang lain ya Misalnya kita main dengan probabilitas itu P stop Di ilustrasi ini dibilang ya Jadi kalau probabilitas P stop nya itu 0,2 atau 20% gitu ya Itu maka ada Ada kemungkinan beberapa notes ini oblivious notes itu notes yang susceptible ya Jadi yang mereka belum mendapatkan rumor ya Kalau jadi probabilitas yang P stop nya itu 0,2 Ada kemungkinan beberapa notes ya Itu masih oblivious dia nggak mendapatkan rumor itu Atau nggak mendapatkan message itu Tapi probabilitasnya sangat kecil sekali disini ya Ini kayaknya kurang dari 0,01 Kalaupun kita tingkatkan yang P stop nya ini misalnya menjadi 0,4 ya Jadi 0,4 dari yang infected Atau 40% dari yang terinfeksi itu nggak menyebarkan lagi Mereka menjadi remove gitu ya Itu pun notes-notes yang masih belum mendapatkan rumor itu masih ya kurang dari 5% 0,05 Kita tingkatkan lagi 0,6 0,8 bahkan sampai 100% ya Semua yang infected itu menjadi remove ya Itu pun ternyata Sampai 0,2 saja ya Atau 20% aja yang belum mendapatkan rumor ya Jadi ini Dengan kata lain Gossiping ini sangat efektif untuk menyebarkan message menyebarkan rumor ya Walaupun ada notes-notes yang menjadi remove setelah infected dia kemudian menjadi remove itu pun Tetap jumlah notes yang tidak mendapatkan rumor ini cukup kecil Itu keuntungan dari yang model Gossiping atau yang epidemic ini Jadi skalabilitasnya itu sangat baik ya Jadi karena mekanismenya sederhana Jadi ini skalabilitasnya juga kalau jumlah notesnya makin banyak itu nggak masalah dengan teknik seperti ini Oke Nah yang bagian ini saya skip aja nanti kalian bisa baca ya Saya mau point out yang pentingnya Tentang side effect ya dari algoritma epidemic maupun yang Gossiping Jadi ada side effect yang mungkin nggak terlalu diharapkan ya Itu adalah kesulitan kalau kita mau menghapus pesan ya Jadi kalau misalnya pesan atau rumor ini sudah disebarkan gitu ya Kemudian ternyata rumornya ini nggak benar gitu ya Jadi kita mau menghapus rumor ini gitu ya Menghapus message-message ini supaya jangan disebarkan lagi ya Supaya jangan disebarkan lagi karena ini hoax misalnya ya Jadi hal yang salah jadi kita nggak perlu sebarkan ulang ya Itu sulit dilakukan ya Kenapa yang melakukan deletion atau penghapusan rumor ini sulit dilakukan karena statusnya gini Kalau misalnya kita menghapusnya itu dengan membersihkan dari satu note ya Jadi satu note ini misalnya terinfeksi Kemudian dia akan berusaha untuk menyebarkan rumor ini ke tetangga-tetangga yang lain Yang belum mendapatkan rumor kan Dia akan coba gitu ya Nah misalnya kemudian kita bilang ini rumornya ini salah hoax gitu ya Jadi kemudian kita mau stok Jadi kita hapus jadi yang note yang infected ini kita hapus rumornya sehingga dia menjadi yang susceptible Statusnya mestinya kan berubah karena dia nggak dapatkan pesan lagi Dia nggak memegang pesan itu, nggak memegang rumor itu Jadi dia statusnya menjadi susceptible Nah akan besar kemungkinan yang susceptible ini dia akan mendapatkan rumor yang sama Jadi rumor yang kita mau stop ini, mau hentikan ini Kita bersihkan dari note-note yang infected Sehingga yang note-note ini menjadi susceptible Yang susceptible ini kemungkinan akan menjadi infected lagi karena dia terkena lagi yang rumor dari note-note lain yang belum sempat kita bersihkan Jadi sangat sulit untuk membersihkan rumor ya Ini kondisinya sama seperti yang kondisi real ya Jadi kalau sekali rumor itu keluar ya Sangat-sangat sulit lah untuk menghentikan rumor ya Walaupun rumor itu rumor yang salah ya Ya ini sama jadi kondisinya seperti itu Ini yang kita bilang sebagai side effect Jadi sulit ya Jadi ya lesson-nya itulah hati-hati ya kalau mau menyebarkan rumor Apalagi rumor yang nggak benar Oke Nah bagaimana ini bisa dilakukan di teknik ini Kita nggak bisa melakukan penghapusan, deletion dari rumor atau message ya Yang kita bisa lakukan rumor message yang salah ini Kita override ya Kita tumpuk atau kita tambahkan lagi dengan message yang baru Jadi ada message baru yang menggantikan message yang lama Tadi kan message-message kan ada timestamp-nya atau ada versinya ya Jadi kita berikan yang message yang lebih baru Dan message yang lebih baru ini bisa kita bilang itu mengoreksi yang salah tadi Ya Nah yang kita lakukan yang message yang baru itu untuk menghapus data yang lama itu Yang kita sebarkan itu kita sebut sebagai Death Certificate Ya surat kematian Ya jadi pesan rumor-rumor yang sudah bergerak itu Kita sertai dengan Death Certificate Untuk rumor tersebut Death Certificate ini jadi akan spesifik ya Ke pesan atau ke rumor yang mana Ya Nah ini kita sebarkan sekalian Ini kan jadi Death Sixticate akan menyebar seperti gosip gitu Ya Harapannya ini sebar jadi ya Semua yang infected Itu akan mendapatkan Death Certificate Ya kemudian dia Ya ini karena rumornya dibilang sudah dead ya Dia kemudian nggak menyebarkan lagi ya Yang dia sebarkan yang Death Certificate nya aja yang dia sebarkan yang lebih baru Ya jadi yang Death Certificate akan dikirimkan ke rumor-rumor yang lainnya ya Yang Death Certificate akan dikirimkan ke not-not lain yang mungkin belum mendapatkan Ya dengan cara ini akhirnya yang rumornya itu Nggak disebarkan lagi karena akan ada yang lebih baru ya Death Certificate nya yang kemudian disebarkan Oke gitu ya caranya jadi Cukup cukup sulit ya menghapus rumor yang sudah terlanjur keluar Oke Nah bisa jadi yang Death Certificate itu kalau sudah cukup lama Bisa jadi Death Certificate nya itu sudah terlalu banyak ya 후� konon pratik Cukup selalu тради L operated Cukup selalu тради untuk memastikan bahwa yang dead certificate ini untuk menghabuskan untuk meng-counter rumor ya jangan sampai kalau dead certificate-nya itu nanti dihilangkan yang dormant ya ini setelah dihilangkan malah rumornya itu bergerak lagi gitu ya supaya jangan sampai begitu biasanya tetap ada beberapa ada node ya beberapa node yang tetap memegang dead certificate itu jadi tidak dibersihkan keseluruhan ya, jadi masih ada beberapa ini dibilang ya, few nodes maintain dormant dead certificate jadi untuk jaga-jaga ya supaya nanti kalau misalnya ternyata rumor yang salah itu muncul kembali ya kemudian ya karena ada dead certificate ini itu menyebar kembali yang dead certificate-nya oke, itu yang terakhir menurut saya ya, itu yang terakhir terkait dengan yang gossip based data dissemination ini ya, oke, nanti kalau ada pertanyaan nanti saat kita ketemu di kelas silakan ditanyakan ya terima kasih"""

DUMMY_MATERIAL = """Distributed Systems 
Communication 
Lecture 04Fundamentals (1)
Interprocess communication is at the heart of all DSes
Due to the absence of shared memory, all 
communication in DSes is based on sending and 
receiving (low level) messages
Communication through message passing is harder 
than using primitives based on shared memory
Modern DSes often consist of thousands or even millions of 
processes scattered across an unreliable network
Many different agreements (e.g., protocols) are needed 
between the communicating parties, varying from the low -
level details of bit transmission to the high -level details of 
how information is to be expressed
Distributed Systems 2Fundamentals (2)
Basic networking model
For many DSes , the lowest -level interface is that of the 
network layer
Distributed Systems 3
Fundamentals (3)
Transport Layer: provides the actual communication 
facilities for most DSes
TCP: connection -oriented, reliable, stream -oriented 
communication 
UDP: unreliable (best -effort) datagram communication 
RTP (Real -time Transport Protocol): specifies packet 
formats for real -time data without providing the actual 
mechanisms for guaranteeing data delivery, and specifies a 
protocol for monitoring and controlling data transfer 
SCTP (Streaming Control Transmission Protocol): groups 
data into messages (i.e., an alternative to TCP that merely 
moves bytes between processes) 
Distributed Systems 4Fundamentals (4)
Middleware protocols: provide common services and 
protocols that can be used by many different apps
A rich set of 
communication protocols
(Un)marshaling of data, 
necessary for integrated 
systems 
Naming protocols to allow 
easy sharing of resources 
Security protocols for 
secure communication 
Scaling mechanisms , such 
as for replication & caching 
Distributed Systems 5
Adapted reference model 
for networked communication Fundamentals (5)
Types of communication
Persistent communication →the message that has been 
submitted for transmission is stored by the communication 
middleware as long as it takes to deliver it to the receiver
The sending application need not continue execution after 
submitting the message
The receiving application need not be executing when the 
message is submitted
Transient communication →the message is stored by the 
communication system only as long as the sending and 
receiving applications are executing
The communication system consists of traditional store -and-
forward routers
If it cannot deliver a message, it will simply drop the message
Distributed Systems 6Fundamentals (6)
Types of communication (cont’d)
Asynchronous communication →the sender continues 
immediately after it has submitted its message for 
transmission
Synchronous communication →the sender is blocked until 
its request is known to be accepted
The sender may be blocked until the middleware notifies that it 
will take over transmission of the request
The sender may synchronize until its request has been delivered to 
the intended recipient
The sender may wait until its request has been fully processed, 
i.e., up to the time that the recipient returns a response
Various combinations of persistence and synchronization 
occur in practice, e.g., message -queuing systems, RPCs
Distributed Systems 7Fundamentals (7)
Types of communication (cont’d) 
Distributed Systems 8
Fundamentals (8)
Types of communication (cont’d)
Discrete communication →the parties communicate by 
messages, each of which forms a complete unit of 
information
Streaming communication →sending multiple messages, 
one after another, where the messages are related to each 
other by the order they are sent, or because there is a 
temporal relationship
Distributed Systems 9Remote Procedure Call (1)
Many DSes have been based on explicit message 
exchange between processes ;  however, the send and 
receive do not conceal communication at all (i.e., no 
access transparency)
Birrell and Nelson [1984] suggested to allow programs 
to call procedures located on other machines ;  this 
method is known as Remote Procedure Call (RPC)
The basic idea sounds simple and elegant, but subtle 
problems exist
They execute in different address space, and parameters & 
results have to be passed, which can be complicated if the 
machines are not identical
Either or both machines can crash & cause more problems
Distributed Systems 10Remote Procedure Call (2)
Conventional procedure call
Consider operation newlist = append(data, dbList);
The purpose is to take a globally defined list object (i.e., 
dbList ) and append a single data element to it (i.e., data ) 
In various programming languages, dbList is a reference to 
a list object, whereas data may be represented by its value 
When calling append , both the 
representations of data and 
dbList are pushed onto the 
stack, making them accessible to 
the implementation of append
Variable data follows a call-by-
value policy and variable dbList
a call-by-reference
Distributed Systems 11
Remote Procedure Call (3)
Conventional procedure call (cont’d)
A value parameter is just an initialized local variable;  the 
called procedure may modify it, but do not affect the 
original at the calling side 
A reference parameter is a pointer to a variable, so the 
address of the variable as stored in main memory is pushed 
onto the stack;  when a call to append adds the value of 
data to dbList , the list object in main memory is modified 
The difference between call -by-value and call -by-reference 
is quite important for RPC
The decision of which parameter passing mechanism to use 
is made by the language designers & a fixed property of the 
language
Distributed Systems 12Remote Procedure Call (4)
Client and server stubs
The idea behind RPC is to make it look as much as possible 
like a local one ;  i.e., make it transparent –the calling 
procedure should not be aware that the called procedure 
is executing on a different machine or vice versa
When append is actually a remote procedure, a different 
version of append–called a client stub –is offered
It is called using the normal calling 
sequence like the original one
It does not perform an append
operation; instead, it packs the 
parameters into a message and 
requests that message to be sent 
to the remote server
Following the call to send , the client stub calls receive , blocking 
itself until the reply comes back
Distributed Systems 13
Remote Procedure Call (5)
Client and server stubs (cont’d)
When the message arrives at the server , the server’s OS 
passes it up to a server stub (i.e., the server -side equivalent 
of a client stub)
Typically the server stub will have called receive and be blocked 
waiting for incoming messages 
It transforms requests coming in over the network into local 
procedure calls 
The server performs its work and returns the result to the caller 
(i.e., server stub) 
When the server stub gets control back, it packs the result in a 
message and calls send to return it to the client 
After that, the server stub usually does a call to receive again 
When the message arrives at the client machine , the OS 
passes it to the client stub , which returns it to the caller 
Distributed Systems 14Remote Procedure Call (6)
Client and server stubs (cont’d)
Distributed Systems 15
  Client  rocedure calls client stub  
  Stub builds  essa e calls local OS 
  OS sends  essa e to re ote OS  
   e ote OS  ives  essa e to stub  
  Stub un ac s  ara eter s calls server   Server does local call returns result to stub  
  Stub builds  essa e  calls OS 
  OS sends  essa e to client  s OS 
  Client s OS  ives  essa e to stub  
   Client stub un ac s result  returns to client Remote Procedure Call (7)
Parameter passing
Packing parameters into a message is called parameter 
marshaling
There is more than just wrapping parameters into a message 
Client and server machines may have different data representations
(i.e., byte ordering –little vs. big endian) 
Wrapping a parameter means transforming a value into a sequence 
of bytes
Client and server have to agree on the same encoding : 
How are basic data values represented (integers, floats, characters) 
How are complex data values represented (arrays, unions) 
Both need to properly interpret messages →transforming them into 
machine -independent representations
Distributed Systems 16Remote Procedure Call (8)
Para eter  assin  (cont’d)
How are pointers, or in general, references passed ?
One solution is to forbid pointers & reference params in general
Another strategy is to copy the array (according to its size) into the 
message and send it to the server;  in effect, call -by-reference has 
been replaced by call -by-copy/restore
When the client stub knows the referred data will be only read, 
there is no need to copy it back when the call has finished 
Using global references (i.e., meaningful to the calling and the 
called processes);  e.g., if the client and the server have access to 
the same file system, a file handle (instead of a pointer) is passed 
Distributed Systems 17Remote Procedure Call (9)
Variations on RPC: Asynchronous RPC
The server immediately sends a reply back to the client the 
moment the RPC request is received ;  the reply acts as an 
acknowledgement to the client
The client will continue without further blocking as soon as 
it has received the server’s ac nowled e ent
Deferred synchronous RPC
→combining an async RPC 
with a callback 
One-way RPC→client 
does not wait for an ack 
Distributed Systems 18
Remote Procedure Call (10)
Variations on RPC: Multicast RPC
Executing multiple RPCs at the same time →adopting the 
one-way RPCs to send an RPC request to a group of servers 
Issues to consider : 
The client app may be unaware 
that an RPC is actually being
forwarded to multiple servers 
(e.g., to increase fault tolerance, 
have all operations executed by 
a backup server who can take 
over when the main server fails) 
Will the client proceed after all 
responses have been received, 
or wait just for one?  It depends 
whether the server has been replicated for fault tolerance or to do 
the same work but on different parts of the input 
Distributed Systems 19
Message -Oriented Communication
RPC and remote object invocations are not always 
appropriate, particularly when it cannot be assumed 
that the receiving side is executing at the time a 
request is issued
Messaging or message -oriented communication is an 
alternative communication service to RPCs
Two types of message -oriented communication:
Message -oriented transient communication
Message -oriented persistent communication
Distributed Systems 20Msg -Oriented Transient Comm. (1)
Many distributed systems and applications are built 
directly on top of the simple message -oriented 
model offered by the transport layer
Standard interfaces have been introduced to the 
transport layer to allow programmers to make use of 
its entire suite of (messaging) protocols through a 
simple set of operations
The standard interfaces also make it easier to port an 
application to a different machine
An example is the sockets interface introduced in the 
1970s in Berkeley UNIX, known as Berkeley Sockets
Distributed Systems 21Msg -Oriented Transient Comm. (2)
Berkeley sockets
Conceptually, a socket is a communication end point to 
which an application can write data that are to be sent out 
over the underlying network, and from which incoming 
data can be read
A socket forms an abstraction over the actual port that is 
used by the local OS for a specific transport protocol (e.g., 
TCP)
Servers generally execute the first four operations (i.e., 
socket , bind , listen , and accept ), normally in the order 
given
Distributed Systems 22Msg -Oriented Transient Comm. (3)
Ber eley soc ets (cont’d)
When calling the socket operation , the caller creates a new 
comm. end point for a specific transport protocol
Internally, it means that the local OS reserves resources to 
accommodate sending and receiving messages for the specified 
protocol
The bind operation associates a local address with the 
newly -created socket , e.g., a server should bind the IP 
address of its machine together with a (possibly well -
known) port number to a socket
Binding tells the OS that the server wants to receive messages only 
on the specified address and port
Distributed Systems 23Msg -Oriented Transient Comm. (4)
Ber eley soc ets (cont’d)
The listen operation is called only in the case of 
connection -oriented communication
It is a non -blocking call that allows the local OS to reserve enough 
buffers for a specified maximum number of pending connection 
requests that the caller is willing to accept
A call to accept blocks the caller until a connection request 
arrives
When a request arrives, the local OS creates a new socket with the 
same properties as the original one, and returns it to the caller
This approach will allow the server to, for example, fork a process 
that will subsequently handle the actual comm. through the new 
connection;  the server, in the meantime, can go back and wait for 
another connection request on the original socket
Distributed Systems 24Msg -Oriented Transient Comm. (5)
Ber eley soc ets (cont’d)
At the client side , the order of execution is as the following
A socket must first be created using the socket operation, but 
explicitly binding the socket to a local address is not necessary, 
since the OS can dynamically allocate a port when the connection 
is set up
The connect operation requires that the caller specifies the 
transport -level address to which a connection request is to be 
sent;  the client is blocked until a connection has been set up 
successfully
After that, both sides can start exchanging information through 
the send and receive operations
Finally, closing a connection is symmetric when using sockets, and 
is established by having both the client and server call the close
operation
Distributed Systems 25Msg -Oriented Transient Comm. (6)
Ber eley soc ets (cont’d)
Distributed Systems 26
                    
      
    
      
      
       
    
       
                                         
                                
                                                        
                             
                                          
                                          
                                  
                                     
                      
Msg -Oriented Transient Comm. (7)
Sockets are rather low level and programming 
mistakes are easily made
More advanced approaches for msg -oriented comm. 
is needed to: 
make network programming easier 
expand beyond the functionality offered by existing 
networking protocols 
make better use of local resources 
etc. 
Distributed Systems 27Msg -Oriented Transient Comm. (8)
ZeroMQ
Provides a higher level of expression by pairing sockets : 
one for sending messages and a corresponding one for 
receiving messages 
Supports many -to-one and one-to-many communication
All communication is asynchronous
Three communication patterns supported: 
Request -reply–used intraditional client -server communication
Publish -subscribe –clients subscribe to specific messages that are 
published by servers
Pipeline–a process wants to push out its results , assuming that 
there are other processes that want to pull in those results
Distributed Systems 28Msg -Oriented Transient Comm. (9)
Sockets were deemed insufficient for communication 
in high -performance multicomputers :
They were at the wrong level of abstraction by supporting 
only simple send and receive operations 
Sockets had been designed to communicate across networks 
using general -purpose protocol stacks (e.g., TCP/IP), not 
suitable for the proprietary protocols for high -speed 
interconnection networks
The need to be hardware and software independent 
eventually led to the definition of a standard called the 
Message -Passing Interface (MPI)
Designed for parallel apps and tailored to transient comm.
Make direct use of the underlying network
Assume that serious failures do not require auto recovery
Distributed Systems 29Msg -Oriented Transient Comm. (10)
Message -Passing Interface
MPI assumes that comm. takes place within a known 
group of processes ;  each group is assigned an identifier, 
and each process within a group is also assigned a (local) id
A (groupID , processID ) pair uniquely identifies the source 
or destination of a message , and is used instead of a 
transport -level address
There may be several, overlapping groups of processes 
involved in a computation and that are all executing at the 
same time
At the core of MPI are messaging operations to support 
transient comm. , of which the most intuitive ones are 
discussed in the following slides
Distributed Systems 30Msg -Oriented Transient Comm. (11)
Message -Passing Interface (cont’d)
The MPI_SEND operation –which is implementation 
dependent –is a blocking send operation that may block 
the caller either until the specified message has been 
co ied to the MPI runti e syste  at the sender’s side, or 
until the receiver has initiated a receive operation
The MPI_BSEND operation supports transient async comm.
The sender submits a message for transmission, which is generally 
first copied to a local buffer in the MPI runtime system
When the message has been copied, the sender continues
The local MPI runtime system will remove the message from its 
local buffer and take care of transmission as soon as a receiver has 
called a receive primitive
The MPI_SSEND operation is sync comm. by which the 
sender blocks until its request is accepted for further 
processing
Distributed Systems 31Msg -Oriented Transient Comm. (12)
Message -Passing Interface (cont’d)
The MPI_SENDRECV operation gives the strongest form of 
sync comm. , in which it sends a request to the receiver and 
blocks until the latter returns a reply ;  basically, it 
corresponds to a normal RPC
The MPI_ISEND operation is a variant of MPI_SEND that 
supports async comm., in which the sender passes a 
pointer to the message (i.e., avoiding copying messages 
from user buffers to buffers internal to the local MPI 
runtime system) and immediately continues
Likewise, the MPI_ISSEND operation is the async variant of 
MPI_SSEND , in which the sender  asses only a  essa e’s 
pointer to the MPI runtime system and continues after the 
runtime system indicates it has processed the message
Distributed Systems 32Msg -Oriented Transient Comm. (13)
Message -Passing Interface (cont’d)
The MPI_RECV operation is called to receive a message ;  
it blocks the caller until a message arrives
The MPI_IRECV operation is the async variant , by which a 
receiver indicates that it is prepared to accept a message
Distributed Systems 33
                    
                                                       
                                                                      
                                                          
                                             
                                                         
                                                                           
                                                 
                                                                Msg -Oriented Persistent Comm. (1)
Message -queuing systems , often called Message -
Oriented Middleware (MOM) , provide extensive 
support for persistent async comm.
They offer intermediate -term storage capacity for messages , 
without requiring either the sender or receiver to be active 
during message transmission
They are typically targeted to support message transfers 
that are allowed to take minutes instead of seconds or 
milliseconds
The basic idea is that applications communicate by 
inserting messages in specific queues
The messages are forwarded over a series of comm. 
servers and are eventually delivered to the destination 
(which could be down)
Distributed Systems 34Msg -Oriented Persistent Comm. (2)
In practice, most comm. servers are directly connected 
to each other ;  so, a message is generally transferred 
directly to a destination server
In principle, each application has its own private queue
to which other applications can send messages;  the 
queue can be read only by its associated application, 
but it is also possible for multiple applications to share 
a single queue
A sender is generally given only the guarantees that its 
 essa e will eventually be inserted in the reci ient’s 
queue ;  no guarantees about when, or even if the 
message will actually be read
The sender & receiver can execute independently
Distributed Systems 35Msg -Oriented Persistent Comm. (3)
Four combinations for loosely coupled communication
Distributed Systems 36
Msg -Oriented Persistent Comm. (4)
The only important aspect from the perspective of 
middleware is that messages are properly addressed
Addressing is done by providing a system -wide unique 
name of the destination queue
Message size may be limited in some cases, although it is 
also possible that the underlying system takes care of 
fragmenting and assembling large messages in a way that 
is completely transparent to applications
The PUT operation is a nonblocking call called by a 
sender to pass a message to the underlying system 
that is to be appended to the specified queue
The GET operation is a blocking call by which an 
authorized process can remove the longest pending 
message in the specified queue
Distributed Systems 37Msg -Oriented Persistent Comm. (5)
Variations of the GET call allow searching for a 
specific message in the queue , e.g., using a priority 
or a matching pattern
The nonblocking variant is given by the POLL
operation, which simply continues if the queue is 
empty or if a specific message could not be found
Most queuing systems also allow a process to install 
a handler as a callback function (through a NOTIFY
operation), automatically invoked whenever a 
message is put into the queue
Callbacks can also be used to automatically start a process –if 
none is executing –that will fetch messages from the queue
Often implemented by means of a daemon that monitors the 
queue for incoming messages and handles accordingly
Distributed Systems 38Msg -Oriented Persistent Comm. (6)
It is the responsibility of a message -queuing system
to provide queues to senders & receivers and take 
care that messages are transferred from their source 
to their destination queue
The collection of queues is distributed across 
multiple machines ;  thus, a message -queuing system 
should maintain a (possibly distributed) database 
that maps queue names to network locations
Distributed Systems 39
                    
                                  
                                                                  
                                                                 
                                                                      Msg -Oriented Persistent Comm. (7)
Queues are managed by queue managers
Normally, a queue manager interacts directly with the 
application that is sending or receiving a message
Some special queue managers operate as routers or relays
as they forward incoming messages to other managers
A message -queuing system may gradually grow into a 
complete, application -level, overlay network
Distributed Systems 40
Msg -Oriented Persistent Comm. (8)
An important application area of message -queuing 
systems is integrating existing and new applications 
into a single, coherent distributed system
It requires that applications can understand the messages 
they receive ;  it requires the sender to have its outgoing 
messages in the same format as that of the receiver
The problem is that each time an application requiring a 
separate messaging protocol is added to the system, other 
application communicating with it will need to provide the 
means for converting their respective messages
An alternative is to agree on a common messaging 
protocol ;  however, it makes sense only if the 
collection of processes that make use of that 
protocol indeed have enough in common
Distributed Systems 41Msg -Oriented Persistent Comm. (9)
The general approach is to learn to live with 
differences , and try to provide the means to make 
conversions as simple as possible
Conversions are handled by message brokers
A message broker acts as an application -level gateway in a 
message -queuing system;  a message broker is generally 
not considered an integral part of the queuing system
It can be as simple as a reformatter for messages , e.g., 
changing record delimiters and field formats
It may handle conversion between two different database 
applications
More common is its use for advanced enterprise 
application integration (EAI) , like matching apps based on 
the messages being exchanged (i.e., pub -sub model) 
Distributed Systems 42Msg -Oriented Persistent Comm. (10)
At the heart of a message broker lies a repository of 
rules for transforming a message of one type to 
another;  the problem is defining the rules and 
developing the plugins
Distributed Systems 43
Example: AMQP (1)
Advanced Message -Queuing Protocol was intended to play 
the same role as, e.g., TCP in networks: a protocol for high -
level messaging with different implementations
Implementations of 
AMQP: RabbitMQ & 
A ache’s ActiveMQ 
AMQP revolves 
around applications, 
queue managers, 
and queues
Basic model: 
App sets up a connection (i.e., a container for a number of one-way 
channels ) to a queue manager ;  two one -way channels form a session
A linkis akin to a socket and maintains state about message transfers
Distributed Systems 44
Example: AMQP (2)
When a message is to be transferred, the app passes it to local 
AMQP stub;  message transfer normally proceeds in 3 steps : 
At the sender’s side, the message is assigned a unique ID and is 
recorded locally to be in an unsettled state . The stub subsequently 
transfers the message to the server , where the AMQP stub also 
records it as being in an unsettled state. Then, the server -side stub 
passes it to the queue manager . 
The receiving app (i.e., queue manager) is assumed to handle the 
message and normally reports back to its stub that it is finished . The 
stub passes this info to the original sender , at which point the message 
at the ori inal sender’s AMQP stub enters a settled state . 
The AMQP stub of the original sender now tells the stub of the original 
receiver that message transfer has been settled (i.e., the original 
sender will for et about the  essa e fro  now on)  The receiver’s 
stub can now also discard anything about the message , formally 
recording it as being settled as well. 
Distributed Systems 45Multicast Communication (1)
Multicast communication in DSes is the support for 
sending data to multiple receivers
For many years, this topic has belonged to the domain of 
network protocols;  some are network -level solutions and 
the others are transport -level solutions
A major issue in all solutions is setting up the comm. paths 
for information dissemination ;  a huge management effort 
is involved, human intervention is required in many cases
With the advent of P2P technology , and notably 
structured overlay management, it becomes easier 
to set up comm. paths ;  as P2P solutions are typically 
deployed at the application layer, various application -
level multicasting techniques have been introduced
Distributed Systems 46Multicast Communication (2)
Application -level multicasting
Basic idea: nodes are organized into an overlay network , 
which is then used to disseminate info to its members
Network routers are not involved in group membership;  
consequently, the connections between nodes in the 
overlay network may cross several physical links, and as 
such, routing messages may not be optimal
Two approaches in the construction of the overlay network
Nodes may organize themselves directly into a tree , meaning that 
there is a unique (overlay) path between every pair of nodes
Nodes may organize into a mesh network , in which every node will 
have multiple neighbors and, in general, there exist multiple paths 
between every pair of nodes
The latter provides higher robustness
Distributed Systems 47Multicast Communication (3)
Application -level  ulticastin  (cont’d)
Building a tree is not difficult once we have organized the 
nodes into an overlay, but building an efficient tree may be 
a different story
The figure shows a set of five nodes organized in a simple 
overlay network ;  node Ais the root of a multicast tree
Whenever Amulticasts a msg to 
the other nodes, the msg will 
traverse links < B, Rb>, <Ra, Rb>, 
<E, Re>, <Rc, Rd>, <D, Rd> twice
The overlay network would have 
been more efficient if we had not 
constructed overlay links < B, E> & 
<D, E>, but instead < A, E> & < C, E> 
Distributed Systems 48
Multicast Communication (4)
Application -level  ulticastin  (cont’d)
The quality of an application -level multicast tree is 
generally measured by three different metrics :
Link stress →counts how often a packet crosses the same link
(when it is greater than 1, it means a packet may be forwarded 
along two different connections at a logical level, but part of those 
connections may actually correspond to the same physical link)
Stretch or Relative Delay Penalty (RDP) →measures the ratio of 
the delay between two nodes in the overlay against the delay that 
those two nodes would experience in the underlying network
(when constructing an overlay network, the goal is to minimize the 
aggregated stretch or the avg RDP measured over all node pairs)
Tree cost →a global metric related to minimizing the aggregated 
link costs (e.g., if the cost is taken to be the delay, then optimizing 
the tree cost boils down to finding a minimal spanning tree in 
which the total time for disseminating info to all nodes is minimal)
Distributed Systems 49Multicast Communication (5)
Application -level  ulticastin  (cont’d)
Switch -trees solution
Assume we have a multicast tree with a single source as root
In this tree, a node Pcan switch parents by dropping the link to its 
current parent in favor of a link to another node ;  constraints are:
The new parent can never be a member of the subtree rooted at P
(as this would partition the tree and create a loop)
The new parent will not have too many immediate children (to limit 
the load of forwarding messages by any single node)
Different criteria for deciding to switch parents :
Optimizing the route to the source;  to this end, each node regularly 
receives info on other nodes so it can evaluate whether another 
node would be a better parent
The delay to the potential other parent is lower than to the current 
parent;  this simple scheme is a reasonable heuristic leading to a 
good approximation of a minimal spanning tree
Distributed Systems 50Multicast Communication (6)
Application -level  ulticastin  (cont’d)
Switch -trees solution (cont’d)
For an example:
Node Preceives info on the neighbors of its parent;  the neighbors 
consists of P’s  rand arent and the other siblin s of P’s  arent
Node Pcan then evaluate the delays to each of these nodes and 
choose the one with the lowest delay, say Q, as its new parent;  
to that end, it sends a switch request to Q
To prevent loops from being formed due to concurrent switching 
requests, a node that has an outstanding switch request will simply 
refuse to process any incoming requests;  in effect, only completely 
independent switches can be carried out simultaneously
Whenever a node notices that its parent has failed , it simply 
attaches itself to the root ;  at that point, the optimization protocol 
can proceed as usual and will eventually place the node at a good 
point in the multicast tree
Distributed Systems 51Multicast Communication (7)
Flooding -based multicasting 
Psimply sends a message 
mto each of its neighbors
Each neighbor will forward 
that message, except to P, 
and only if it had not seen 
mbefore
Variation ( probabilistic broadcasting ): Let Qforward a 
message with a probability Pflood, possibly even dependent 
on its own number of neighbors (i.e., node degree) or the 
degree of its neighbors 
In a random network of 10,000 nodes and Pedge= 0.1, we need only 
set Pflood= 0.01 to establish a more than 50 -fold reduction in the 
number of messages sent in comparison to full flooding 
Distributed Systems 52
Multicast Communication (8)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay (i.e., deterministic 
topology), designing efficient flooding schemes is simpler
Consider a 4 -dimensional hypercube 
A simple and efficient broadcast 
scheme relies on keeping track of 
neighbors per dimension
A node initially broadcasts a message 
mto all of its neighbors and tags m
with the label (i.e., dimension) of the 
edge over which it sends the message 
For example: If node 1001 broadcasts a message m, it will send ( m,1) 
to 0001, ( m,2) to 1101, ( m,3) to 1011, ( m,4) to 1000. When a node 
receives a broadcast message, it will forward it only along edges with 
a higher dimension. So, node 1101 will send ( m,3) to 1111 and ( m,4) 
to 1100. It can be shown that every broadcast requires precisely N−  
messages (where N= 2n= the no. of nodes in an n-dim hypercube) 
Distributed Systems 53
Multicast Communication (9)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay … (cont’d) 
Consider a 5 -bit Chord 
Assume that node 9 wants to flood a 
message to all other nodes 
Node 9 divides the ID space into four 
segments (one for each of its neighbors): 
node    ta es care of nodes ID    ≤ k< 14, 
node    for    ≤ k< 18, node 18 for 
   ≤ k<   , and node    for    ≤ k< 9 
Node 28 will subsequently divide the part 
of the ID space it is requested to handle 
into two subsegments: [1,4) and [4,9) 
Node 18 will split its segment into only one 
part and forward the message to [20,28) 
Lastly, node 20 forwards the message to 
[21,28) 
Distributed Systems 54
Multicast Communication (10)
Gossip -based data dissemination
An increasingly important technique for disseminating info
is to rely on epidemic behavior ;  epidemics studies the 
spreading of infectious diseases
The main goal is to rapidly propagate info among a large 
collection of nodes using only local info;  there is no central 
component by which info dissemination is coordinated
Using the terminology from epidemics:
A node that is part of a DS is called infected if it holds data that it is 
willing to spread to other nodes
A node that has not yet seen this data is called susceptible
An updated node that is not willing or able to spread its data is 
said to be removed
Distributed Systems 55Multicast Communication (11)
Gossip -based data disse ination (cont’d)
We can distinguish old from new data, e.g., because it has 
been timestamped or versioned
A popular propagation model is that of anti-entropy ;  in 
this model, a node Ppicks another node Qat random, and 
subsequently exchanges updates with Qusing one of these 
three approaches :
Ponly pushes its own updates to Q
Ponly pulls in new updates from Q
Pand Qsend updates to each other (i.e., a push -pull approach)
When it comes to rapidly spreading updates, only pushing 
updates turns out to be a bad choice ;  if many nodes are 
infected, the probability of one selecting a susceptible 
node is relatively small
Distributed Systems 56Multicast Communication (12)
Gossip -based data disse ination (cont’d)
The pull -based approach works much better when many 
nodes are infected ;  chances are big that a susceptible 
node will contact an infected one to subsequently pull in 
the updates and become infected as well
If only a single node is infected, updates will rapidly spread 
across all nodes using either form of anti -entropy, although 
push -pull remains the best strategy
Propagating a single update to all nodes takes 𝒪(log(N)) 
rounds, where Nis the number of nodes;  this indicates 
that propagating updates is fast, but above all scalable
One special variant of this approach is called rumor 
spreading , or simply gossiping
Distributed Systems 57Multicast Communication (13)
Gossip -based data disse ination (cont’d)
Gossiping
If node Phas just been updated for data 
item x, it contacts an arbitrary other node 
Qand tries to push the update to Q
However, it is possible that Qwas already 
updated by another node;  in that case, P
may lose interest in spreading the update 
any further (with probability pstop), it then becomes removed
It is an excellent way of rapidly spreading news ;  however, it 
cannot guarantee that all nodes will actually be updated
One of the main advantages of epidemic algorithms is 
their scalability , due to the fact that the number of sync. 
between processes is relatively small compared to other 
propagation methods
Distributed Systems 58
Multicast Communication (14)
Gossip -based data disse ination (cont’d)
For wide -area systems, it makes sense to take the actual 
network topology into account to achieve better results
Nodes that are connected to only a few other nodes are contacted 
with a relatively high probability 
Assumption: such nodes form a bridge to other remote parts of 
network;  therefore, they should be contacted as soon as possible
This approach is referred to as directional gossiping
Most epidemic solutions assume that a node can randomly 
select any other node to gossip with
This implies that, in principle, the complete set of nodes should be 
known to each member;  in a large system, this can never hold
Fortunately, maintaining a partial view that is more or less 
continuously updated will organize the collection of nodes into a 
random graphDistributed Systems 59Multicast Communication (15)
Gossip -based data disse ination (cont’d)
Epidemic algorithms have a rather strange side -effect: 
spreading the deletion of a data item is hard
The problem lies in the fact that deletion of a data item destroys 
all info on that item
Consequently, when a data item is simply removed from a node, 
the node will eventually receive old copies of the data item and 
interpret those as updates on something it did not have before
The trick is to record the deletion of a data item as just 
another update and keep a record of that deletion
In this way, old copies will not be interpreted as something new, 
but merely treated as versions that have been updated by a delete 
operation
The recording of a deletion is done by spreading death certificates
Distributed Systems 60Multicast Communication (16)
Gossip -based data disse ination (cont’d)
The problem with death certificates is that they should 
eventually be cleaned up , or otherwise each node will 
gradually build a huge local database of historical info on 
deleted data items that actually are not used
Dormant death certificates
Each death cert is timestamped when it is created
If it can be assumed that updates propagate to all nodes within a 
known finite time, then death certs can be removed after this max 
propagation time has elapsed
To provide hard guarantees that deletions are indeed spread to all 
nodes, only a few nodes maintain dormant death certs that are 
never thrown away
Distributed Systems 61RESERVED MATERIALS
Distributed SystemsStream -Oriented Communication (1)
Communication as discussed so far has concentrated 
on exchanging more -or-less independent and 
complete units of information
There are forms of comm. in which timing plays a 
crucial role, e.g., an audio stream built up as a 
sequence of 16 -bit samples
Assume that the audio stream represents CD quality, 
meaning that the original sound wave has been sampled at 
a frequency of 44,100 Hz
To reproduce the original sound, it is essential that the 
samples in the audio stream are played out in the order 
they appear in the stream, but also at intervals of exactly 
1 / 44,100 second
Distributed SystemsStream -Oriented Communication (2)
Support for the exchange of time -dependent info is 
often formulated as support for continuous media
In continuous (representation) media, the temporal 
relationships between different data items are 
fundamental to correctly interpreting what the data 
actually mean , e.g., an audio or video stream
In discrete (representation) media, the temporal 
relationships between data items are not
fundamental to correctly interpreting the data, e.g., 
text, still images, object code or executable files
Distributed SystemsStream -Oriented Communication (3)
To capture the exchange of time -dependent info, 
DSes generally provide support for data streams
A data stream is a sequence of data units
It can be applied to discrete as well as continuous media
UNIX pipes or TCP/IP connections are typical examples of 
(byte -oriented) discrete data streams
Playing an audio file typically requires setting up a 
continuous data stream between the file and the audio 
device
To capture timing aspects, a distinction is often made 
between different transmission modes: 
asynchronous , synchronous , and isochronous
Distributed SystemsStream -Oriented Communication (4)
Asynchronous transmission mode
The data items in a stream are transmitted one after the 
other, but there are no further timing constraints on when 
transmission of items should take place
This is typically the case for discrete data streams
Synchronous transmission mode
There is a maximum end -to-end delay defined for each 
unit in a data stream
It may be important that the end -to-end propagation time 
through the network is guaranteed to be lower that the 
time interval between taking samples, but it cannot do any 
harm if samples are propagated faster than necessary
E.g., a sensor sending sample temperature at a certain rate
Distributed SystemsStream -Oriented Communication (5)
Isochronous transmission mode
It is necessary that data units are transferred on time;  this 
means that data transfer is subject to a maximum and 
minimum end -to-end delay, also referred to as bounded 
(delay) jitter
It plays a crucial role in representing audio and video
Streams can be simple or complex
A simple stream consists of only a single sequence of data
A complex stream consists of several related simple 
streams, called substreams ;  the relation between the 
substreams is often also time dependent
Distributed SystemsStream -Oriented Communication (6)
From a DS perspective, we can distinguish several 
elements needed for supporting streams
For simplicity, we concentrate on streaming stored data, as 
opposed to streaming live data
We can sketch a general client -server architecture
Distributed Systems
Stream -Oriented Communication (7)
QoS ro erties fro  an a  lication’s  ers ective:
The required bit rate at which data should be transported
The max delay until a session has been set up (i.e., when 
an application can start sending data) 
The max end -to-end delay (i.e., how long it will take until a 
data unit makes it to a recipient)
The max delay variance, or jitter
The max round -trip delay
When dealing with stream -oriented comm. that is 
based on the Internet protocol stack, the basis of 
comm. is formed by an extremely simple, best -effort 
datagram service (i.e., IP) 
Distributed SystemsStream -Oriented Communication (8)
Given that the underlying system offers only a best -
effort delivery service, a DS can try to conceal as 
much as possible of the lack of QoS
The Internet provides a means for differentiated services;  
a sending host can essentially mark outgoing packets as 
belonging to one of several classes, including an expedited 
forwarding class and an assured forwarding class (by which 
traffic is divided into four subclasses along with three ways 
to drop packets if the network gets congested)
DS may use buffers to 
reduce jitter
Distributed Systems
Stream -Oriented Communication (9)
Given that … (cont’d)
Applying forward error correction (FEC) techniques to 
compensate for the loss in QoS
Since a single packet may contain multiple audio and video 
frames, when it is lost, the receiver may actually perceive a 
large gap when playing out frames;  this can be somewhat 
circumvented by interleaving frames, but this approach 
requires a large receive buffer and thus imposes a higher 
start delay for the receiving application
Distributed Systems
Stream -Oriented Communication (10)
Stream synchronization
Synchronization of streams deals with maintaining 
temporal relations between streams
Sync. between a discrete data stream & a continuous data stream, 
e.g., a slide show enhanced with audio
Sync. between continuous data streams, e.g., a video stream 
synchronized with the audio (lip synchronization), a stereo audio 
stream consisting two substreams
Two issues in stream synchronization:
The basic mechanisms for synchronizing two streams
The distribution of those mechanisms in a networked environment
Sync. mechanisms can be viewed at several different levels 
of abstraction
Distributed SystemsStream -Oriented Communication (11)
Strea  synchronization (cont’d)
At the lowest level, sync. is done explicitly by operating on 
the data units of simple streams
There is a process that simply executes read and write operations 
on several simple streams, ensuring that those operations adhere 
to specific timing and sync. constraints
Consider a movie presented as 
2 input streams (video & audio)
The video stream contains 
uncompressed low -quality 
images of 320 240 pixels, each 
encoded by a single byte, 
leading to video data units of 
76,800 bytes each;  the images 
are to be displayed at 30 Hz, or 
one image every 33 ms
Distributed Systems
Stream -Oriented Communication (12)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
Consider a  ovie … (cont’d)
The 44.1 kHz, 16 -bit, stereo audio stream contains samples grouped 
into units of 5,880 bytes, each corresponding to 33 ms of audio
If the input process can handle 2.5 Mbps, we can achieve lip sync. by 
simply alternating between reading an image and reading a block of 
audio samples every 33 ms;  the drawback of this approach is that the 
application is made completely responsible for implementing sync. 
while it has only low -level facilities available
A better approach is to offer an interface that allows the 
application to more easily control streams and devices
An application developer can write a simple monitor program 
consisting of two handlers, one for each stream, that jointly check if 
the video and audio streams are sufficiently synchronized, and if 
needed, adjust the rate at which video or audio units are presented
Distributed SystemsStream -Oriented Communication (13)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
The last example is typical for multimedia middleware systems
The middleware offers a collection of interfaces for controlling 
audio and video streams, including interfaces for controlling 
devices, e.g., monitors, cameras, microphones, etc.
Each device and stream has 
its own high -level interfaces, 
including interfaces for 
notifying an application 
when some event occurred;  
the latter interfaces are 
subsequently used to write 
handlers for synchronizing 
streams
Distributed Systems
Stream -Oriented Communication (14)
Strea  synchronization (cont’d)
The distribution of synchronization mechanisms
The receiving side of a complex stream needs to know exactly 
what to do;  it must have a complete synchronization specification
locally available
Common practice is to provide this info implicitly by multiplexing the 
different streams into a single stream containing all data units, 
including those for sync.
For an example: the MPEG -2 standard allows an unlimited number of 
continuous and discrete streams to be merged into a single stream
Another issue is whether sync. should take place at the sending or 
receiving side
If the sender handles sync., it may merge streams into a single 
stream with a different type of data units, e.g., a stereo audio stream
The receiver merely has to read in a data unit, and split it into a left 
and right sample;  delays for both channels are now identical
Distributed SystemsDistributed Systems 
Communication 
Lecture 04
Fundamentals (1)
Interprocess communication is at the heart of all DSes
Due to the absence of shared memory, all 
communication in DSes is based on sending and 
receiving (low level) messages
Communication through message passing is harder 
than using primitives based on shared memory
Modern DSes often consist of thousands or even millions of 
processes scattered across an unreliable network
Many different agreements (e.g., protocols) are needed 
between the communicating parties, varying from the low -
level details of bit transmission to the high -level details of 
how information is to be expressed
Distributed Systems 2
Fundamentals (2)
Basic networking model
For many DSes , the lowest -level interface is that of the 
network layer
Distributed Systems 3

Fundamentals (3)
Transport Layer: provides the actual communication 
facilities for most DSes
TCP: connection -oriented, reliable, stream -oriented 
communication 
UDP: unreliable (best -effort) datagram communication 
RTP (Real -time Transport Protocol): specifies packet 
formats for real -time data without providing the actual 
mechanisms for guaranteeing data delivery, and specifies a 
protocol for monitoring and controlling data transfer 
SCTP (Streaming Control Transmission Protocol): groups 
data into messages (i.e., an alternative to TCP that merely 
moves bytes between processes) 
Distributed Systems 4
Fundamentals (4)
Middleware protocols: provide common services and 
protocols that can be used by many different apps
A rich set of 
communication protocols
(Un)marshaling of data, 
necessary for integrated 
systems 
Naming protocols to allow 
easy sharing of resources 
Security protocols for 
secure communication 
Scaling mechanisms , such 
as for replication & caching 
Distributed Systems 5
Adapted reference model 
for networked communication 
Fundamentals (5)
Types of communication
Persistent communication →the message that has been 
submitted for transmission is stored by the communication 
middleware as long as it takes to deliver it to the receiver
The sending application need not continue execution after 
submitting the message
The receiving application need not be executing when the 
message is submitted
Transient communication →the message is stored by the 
communication system only as long as the sending and 
receiving applications are executing
The communication system consists of traditional store -and-
forward routers
If it cannot deliver a message, it will simply drop the message
Distributed Systems 6
Fundamentals (6)
Types of communication (cont’d)
Asynchronous communication →the sender continues 
immediately after it has submitted its message for 
transmission
Synchronous communication →the sender is blocked until 
its request is known to be accepted
The sender may be blocked until the middleware notifies that it 
will take over transmission of the request
The sender may synchronize until its request has been delivered to 
the intended recipient
The sender may wait until its request has been fully processed, 
i.e., up to the time that the recipient returns a response
Various combinations of persistence and synchronization 
occur in practice, e.g., message -queuing systems, RPCs
Distributed Systems 7
Fundamentals (7)
Types of communication (cont’d) 
Distributed Systems 8

Fundamentals (8)
Types of communication (cont’d)
Discrete communication →the parties communicate by 
messages, each of which forms a complete unit of 
information
Streaming communication →sending multiple messages, 
one after another, where the messages are related to each 
other by the order they are sent, or because there is a 
temporal relationship
Distributed Systems 9
Remote Procedure Call (1)
Many DSes have been based on explicit message 
exchange between processes ;  however, the send and 
receive do not conceal communication at all (i.e., no 
access transparency)
Birrell and Nelson [1984] suggested to allow programs 
to call procedures located on other machines ;  this 
method is known as Remote Procedure Call (RPC)
The basic idea sounds simple and elegant, but subtle 
problems exist
They execute in different address space, and parameters & 
results have to be passed, which can be complicated if the 
machines are not identical
Either or both machines can crash & cause more problems
Distributed Systems 10
Remote Procedure Call (2)
Conventional procedure call
Consider operation newlist = append(data, dbList);
The purpose is to take a globally defined list object (i.e., 
dbList ) and append a single data element to it (i.e., data ) 
In various programming languages, dbList is a reference to 
a list object, whereas data may be represented by its value 
When calling append , both the 
representations of data and 
dbList are pushed onto the 
stack, making them accessible to 
the implementation of append
Variable data follows a call-by-
value policy and variable dbList
a call-by-reference
Distributed Systems 11

Remote Procedure Call (3)
Conventional procedure call (cont’d)
A value parameter is just an initialized local variable;  the 
called procedure may modify it, but do not affect the 
original at the calling side 
A reference parameter is a pointer to a variable, so the 
address of the variable as stored in main memory is pushed 
onto the stack;  when a call to append adds the value of 
data to dbList , the list object in main memory is modified 
The difference between call -by-value and call -by-reference 
is quite important for RPC
The decision of which parameter passing mechanism to use 
is made by the language designers & a fixed property of the 
language
Distributed Systems 12
Remote Procedure Call (4)
Client and server stubs
The idea behind RPC is to make it look as much as possible 
like a local one ;  i.e., make it transparent –the calling 
procedure should not be aware that the called procedure 
is executing on a different machine or vice versa
When append is actually a remote procedure, a different 
version of append–called a client stub –is offered
It is called using the normal calling 
sequence like the original one
It does not perform an append
operation; instead, it packs the 
parameters into a message and 
requests that message to be sent 
to the remote server
Following the call to send , the client stub calls receive , blocking 
itself until the reply comes back
Distributed Systems 13

Remote Procedure Call (5)
Client and server stubs (cont’d)
When the message arrives at the server , the server’s OS 
passes it up to a server stub (i.e., the server -side equivalent 
of a client stub)
Typically the server stub will have called receive and be blocked 
waiting for incoming messages 
It transforms requests coming in over the network into local 
procedure calls 
The server performs its work and returns the result to the caller 
(i.e., server stub) 
When the server stub gets control back, it packs the result in a 
message and calls send to return it to the client 
After that, the server stub usually does a call to receive again 
When the message arrives at the client machine , the OS 
passes it to the client stub , which returns it to the caller 
Distributed Systems 14
Remote Procedure Call (6)
Client and server stubs (cont’d)
Distributed Systems 15
  Client  rocedure calls client stub  
  Stub builds  essa e calls local OS 
  OS sends  essa e to re ote OS  
   e ote OS  ives  essa e to stub  
  Stub un ac s  ara eter s calls server   Server does local call returns result to stub  
  Stub builds  essa e  calls OS 
  OS sends  essa e to client  s OS 
  Client s OS  ives  essa e to stub  
   Client stub un ac s result  returns to client 
Remote Procedure Call (7)
Parameter passing
Packing parameters into a message is called parameter 
marshaling
There is more than just wrapping parameters into a message 
Client and server machines may have different data representations
(i.e., byte ordering –little vs. big endian) 
Wrapping a parameter means transforming a value into a sequence 
of bytes
Client and server have to agree on the same encoding : 
How are basic data values represented (integers, floats, characters) 
How are complex data values represented (arrays, unions) 
Both need to properly interpret messages →transforming them into 
machine -independent representations
Distributed Systems 16
Remote Procedure Call (8)
Para eter  assin  (cont’d)
How are pointers, or in general, references passed ?
One solution is to forbid pointers & reference params in general
Another strategy is to copy the array (according to its size) into the 
message and send it to the server;  in effect, call -by-reference has 
been replaced by call -by-copy/restore
When the client stub knows the referred data will be only read, 
there is no need to copy it back when the call has finished 
Using global references (i.e., meaningful to the calling and the 
called processes);  e.g., if the client and the server have access to 
the same file system, a file handle (instead of a pointer) is passed 
Distributed Systems 17
Remote Procedure Call (9)
Variations on RPC: Asynchronous RPC
The server immediately sends a reply back to the client the 
moment the RPC request is received ;  the reply acts as an 
acknowledgement to the client
The client will continue without further blocking as soon as 
it has received the server’s ac nowled e ent
Deferred synchronous RPC
→combining an async RPC 
with a callback 
One-way RPC→client 
does not wait for an ack 
Distributed Systems 18

Remote Procedure Call (10)
Variations on RPC: Multicast RPC
Executing multiple RPCs at the same time →adopting the 
one-way RPCs to send an RPC request to a group of servers 
Issues to consider : 
The client app may be unaware 
that an RPC is actually being
forwarded to multiple servers 
(e.g., to increase fault tolerance, 
have all operations executed by 
a backup server who can take 
over when the main server fails) 
Will the client proceed after all 
responses have been received, 
or wait just for one?  It depends 
whether the server has been replicated for fault tolerance or to do 
the same work but on different parts of the input 
Distributed Systems 19

Message -Oriented Communication
RPC and remote object invocations are not always 
appropriate, particularly when it cannot be assumed 
that the receiving side is executing at the time a 
request is issued
Messaging or message -oriented communication is an 
alternative communication service to RPCs
Two types of message -oriented communication:
Message -oriented transient communication
Message -oriented persistent communication
Distributed Systems 20
Msg -Oriented Transient Comm. (1)
Many distributed systems and applications are built 
directly on top of the simple message -oriented 
model offered by the transport layer
Standard interfaces have been introduced to the 
transport layer to allow programmers to make use of 
its entire suite of (messaging) protocols through a 
simple set of operations
The standard interfaces also make it easier to port an 
application to a different machine
An example is the sockets interface introduced in the 
1970s in Berkeley UNIX, known as Berkeley Sockets
Distributed Systems 21
Msg -Oriented Transient Comm. (2)
Berkeley sockets
Conceptually, a socket is a communication end point to 
which an application can write data that are to be sent out 
over the underlying network, and from which incoming 
data can be read
A socket forms an abstraction over the actual port that is 
used by the local OS for a specific transport protocol (e.g., 
TCP)
Servers generally execute the first four operations (i.e., 
socket , bind , listen , and accept ), normally in the order 
given
Distributed Systems 22
Msg -Oriented Transient Comm. (3)
Ber eley soc ets (cont’d)
When calling the socket operation , the caller creates a new 
comm. end point for a specific transport protocol
Internally, it means that the local OS reserves resources to 
accommodate sending and receiving messages for the specified 
protocol
The bind operation associates a local address with the 
newly -created socket , e.g., a server should bind the IP 
address of its machine together with a (possibly well -
known) port number to a socket
Binding tells the OS that the server wants to receive messages only 
on the specified address and port
Distributed Systems 23
Msg -Oriented Transient Comm. (4)
Ber eley soc ets (cont’d)
The listen operation is called only in the case of 
connection -oriented communication
It is a non -blocking call that allows the local OS to reserve enough 
buffers for a specified maximum number of pending connection 
requests that the caller is willing to accept
A call to accept blocks the caller until a connection request 
arrives
When a request arrives, the local OS creates a new socket with the 
same properties as the original one, and returns it to the caller
This approach will allow the server to, for example, fork a process 
that will subsequently handle the actual comm. through the new 
connection;  the server, in the meantime, can go back and wait for 
another connection request on the original socket
Distributed Systems 24
Msg -Oriented Transient Comm. (5)
Ber eley soc ets (cont’d)
At the client side , the order of execution is as the following
A socket must first be created using the socket operation, but 
explicitly binding the socket to a local address is not necessary, 
since the OS can dynamically allocate a port when the connection 
is set up
The connect operation requires that the caller specifies the 
transport -level address to which a connection request is to be 
sent;  the client is blocked until a connection has been set up 
successfully
After that, both sides can start exchanging information through 
the send and receive operations
Finally, closing a connection is symmetric when using sockets, and 
is established by having both the client and server call the close
operation
Distributed Systems 25
Msg -Oriented Transient Comm. (6)
Ber eley soc ets (cont’d)
Distributed Systems 26
                    
      
    
      
      
       
    
       
                                         
                                
                                                        
                             
                                          
                                          
                                  
                                     
                      

Msg -Oriented Transient Comm. (7)
Sockets are rather low level and programming 
mistakes are easily made
More advanced approaches for msg -oriented comm. 
is needed to: 
make network programming easier 
expand beyond the functionality offered by existing 
networking protocols 
make better use of local resources 
etc. 
Distributed Systems 27
Msg -Oriented Transient Comm. (8)
ZeroMQ
Provides a higher level of expression by pairing sockets : 
one for sending messages and a corresponding one for 
receiving messages 
Supports many -to-one and one-to-many communication
All communication is asynchronous
Three communication patterns supported: 
Request -reply–used intraditional client -server communication
Publish -subscribe –clients subscribe to specific messages that are 
published by servers
Pipeline–a process wants to push out its results , assuming that 
there are other processes that want to pull in those results
Distributed Systems 28
Msg -Oriented Transient Comm. (9)
Sockets were deemed insufficient for communication 
in high -performance multicomputers :
They were at the wrong level of abstraction by supporting 
only simple send and receive operations 
Sockets had been designed to communicate across networks 
using general -purpose protocol stacks (e.g., TCP/IP), not 
suitable for the proprietary protocols for high -speed 
interconnection networks
The need to be hardware and software independent 
eventually led to the definition of a standard called the 
Message -Passing Interface (MPI)
Designed for parallel apps and tailored to transient comm.
Make direct use of the underlying network
Assume that serious failures do not require auto recovery
Distributed Systems 29
Msg -Oriented Transient Comm. (10)
Message -Passing Interface
MPI assumes that comm. takes place within a known 
group of processes ;  each group is assigned an identifier, 
and each process within a group is also assigned a (local) id
A (groupID , processID ) pair uniquely identifies the source 
or destination of a message , and is used instead of a 
transport -level address
There may be several, overlapping groups of processes 
involved in a computation and that are all executing at the 
same time
At the core of MPI are messaging operations to support 
transient comm. , of which the most intuitive ones are 
discussed in the following slides
Distributed Systems 30
Msg -Oriented Transient Comm. (11)
Message -Passing Interface (cont’d)
The MPI_SEND operation –which is implementation 
dependent –is a blocking send operation that may block 
the caller either until the specified message has been 
co ied to the MPI runti e syste  at the sender’s side, or 
until the receiver has initiated a receive operation
The MPI_BSEND operation supports transient async comm.
The sender submits a message for transmission, which is generally 
first copied to a local buffer in the MPI runtime system
When the message has been copied, the sender continues
The local MPI runtime system will remove the message from its 
local buffer and take care of transmission as soon as a receiver has 
called a receive primitive
The MPI_SSEND operation is sync comm. by which the 
sender blocks until its request is accepted for further 
processing
Distributed Systems 31
Msg -Oriented Transient Comm. (12)
Message -Passing Interface (cont’d)
The MPI_SENDRECV operation gives the strongest form of 
sync comm. , in which it sends a request to the receiver and 
blocks until the latter returns a reply ;  basically, it 
corresponds to a normal RPC
The MPI_ISEND operation is a variant of MPI_SEND that 
supports async comm., in which the sender passes a 
pointer to the message (i.e., avoiding copying messages 
from user buffers to buffers internal to the local MPI 
runtime system) and immediately continues
Likewise, the MPI_ISSEND operation is the async variant of 
MPI_SSEND , in which the sender  asses only a  essa e’s 
pointer to the MPI runtime system and continues after the 
runtime system indicates it has processed the message
Distributed Systems 32
Msg -Oriented Transient Comm. (13)
Message -Passing Interface (cont’d)
The MPI_RECV operation is called to receive a message ;  
it blocks the caller until a message arrives
The MPI_IRECV operation is the async variant , by which a 
receiver indicates that it is prepared to accept a message
Distributed Systems 33
                    
                                                       
                                                                      
                                                          
                                             
                                                         
                                                                           
                                                 
                                                                
Msg -Oriented Persistent Comm. (1)
Message -queuing systems , often called Message -
Oriented Middleware (MOM) , provide extensive 
support for persistent async comm.
They offer intermediate -term storage capacity for messages , 
without requiring either the sender or receiver to be active 
during message transmission
They are typically targeted to support message transfers 
that are allowed to take minutes instead of seconds or 
milliseconds
The basic idea is that applications communicate by 
inserting messages in specific queues
The messages are forwarded over a series of comm. 
servers and are eventually delivered to the destination 
(which could be down)
Distributed Systems 34
Msg -Oriented Persistent Comm. (2)
In practice, most comm. servers are directly connected 
to each other ;  so, a message is generally transferred 
directly to a destination server
In principle, each application has its own private queue
to which other applications can send messages;  the 
queue can be read only by its associated application, 
but it is also possible for multiple applications to share 
a single queue
A sender is generally given only the guarantees that its 
 essa e will eventually be inserted in the reci ient’s 
queue ;  no guarantees about when, or even if the 
message will actually be read
The sender & receiver can execute independently
Distributed Systems 35
Msg -Oriented Persistent Comm. (3)
Four combinations for loosely coupled communication
Distributed Systems 36

Msg -Oriented Persistent Comm. (4)
The only important aspect from the perspective of 
middleware is that messages are properly addressed
Addressing is done by providing a system -wide unique 
name of the destination queue
Message size may be limited in some cases, although it is 
also possible that the underlying system takes care of 
fragmenting and assembling large messages in a way that 
is completely transparent to applications
The PUT operation is a nonblocking call called by a 
sender to pass a message to the underlying system 
that is to be appended to the specified queue
The GET operation is a blocking call by which an 
authorized process can remove the longest pending 
message in the specified queue
Distributed Systems 37
Msg -Oriented Persistent Comm. (5)
Variations of the GET call allow searching for a 
specific message in the queue , e.g., using a priority 
or a matching pattern
The nonblocking variant is given by the POLL
operation, which simply continues if the queue is 
empty or if a specific message could not be found
Most queuing systems also allow a process to install 
a handler as a callback function (through a NOTIFY
operation), automatically invoked whenever a 
message is put into the queue
Callbacks can also be used to automatically start a process –if 
none is executing –that will fetch messages from the queue
Often implemented by means of a daemon that monitors the 
queue for incoming messages and handles accordingly
Distributed Systems 38
Msg -Oriented Persistent Comm. (6)
It is the responsibility of a message -queuing system
to provide queues to senders & receivers and take 
care that messages are transferred from their source 
to their destination queue
The collection of queues is distributed across 
multiple machines ;  thus, a message -queuing system 
should maintain a (possibly distributed) database 
that maps queue names to network locations
Distributed Systems 39
                    
                                  
                                                                  
                                                                 
                                                                      
Msg -Oriented Persistent Comm. (7)
Queues are managed by queue managers
Normally, a queue manager interacts directly with the 
application that is sending or receiving a message
Some special queue managers operate as routers or relays
as they forward incoming messages to other managers
A message -queuing system may gradually grow into a 
complete, application -level, overlay network
Distributed Systems 40

Msg -Oriented Persistent Comm. (8)
An important application area of message -queuing 
systems is integrating existing and new applications 
into a single, coherent distributed system
It requires that applications can understand the messages 
they receive ;  it requires the sender to have its outgoing 
messages in the same format as that of the receiver
The problem is that each time an application requiring a 
separate messaging protocol is added to the system, other 
application communicating with it will need to provide the 
means for converting their respective messages
An alternative is to agree on a common messaging 
protocol ;  however, it makes sense only if the 
collection of processes that make use of that 
protocol indeed have enough in common
Distributed Systems 41
Msg -Oriented Persistent Comm. (9)
The general approach is to learn to live with 
differences , and try to provide the means to make 
conversions as simple as possible
Conversions are handled by message brokers
A message broker acts as an application -level gateway in a 
message -queuing system;  a message broker is generally 
not considered an integral part of the queuing system
It can be as simple as a reformatter for messages , e.g., 
changing record delimiters and field formats
It may handle conversion between two different database 
applications
More common is its use for advanced enterprise 
application integration (EAI) , like matching apps based on 
the messages being exchanged (i.e., pub -sub model) 
Distributed Systems 42
Msg -Oriented Persistent Comm. (10)
At the heart of a message broker lies a repository of 
rules for transforming a message of one type to 
another;  the problem is defining the rules and 
developing the plugins
Distributed Systems 43

Example: AMQP (1)
Advanced Message -Queuing Protocol was intended to play 
the same role as, e.g., TCP in networks: a protocol for high -
level messaging with different implementations
Implementations of 
AMQP: RabbitMQ & 
A ache’s ActiveMQ 
AMQP revolves 
around applications, 
queue managers, 
and queues
Basic model: 
App sets up a connection (i.e., a container for a number of one-way 
channels ) to a queue manager ;  two one -way channels form a session
A linkis akin to a socket and maintains state about message transfers
Distributed Systems 44

Example: AMQP (2)
When a message is to be transferred, the app passes it to local 
AMQP stub;  message transfer normally proceeds in 3 steps : 
At the sender’s side, the message is assigned a unique ID and is 
recorded locally to be in an unsettled state . The stub subsequently 
transfers the message to the server , where the AMQP stub also 
records it as being in an unsettled state. Then, the server -side stub 
passes it to the queue manager . 
The receiving app (i.e., queue manager) is assumed to handle the 
message and normally reports back to its stub that it is finished . The 
stub passes this info to the original sender , at which point the message 
at the ori inal sender’s AMQP stub enters a settled state . 
The AMQP stub of the original sender now tells the stub of the original 
receiver that message transfer has been settled (i.e., the original 
sender will for et about the  essa e fro  now on)  The receiver’s 
stub can now also discard anything about the message , formally 
recording it as being settled as well. 
Distributed Systems 45
Multicast Communication (1)
Multicast communication in DSes is the support for 
sending data to multiple receivers
For many years, this topic has belonged to the domain of 
network protocols;  some are network -level solutions and 
the others are transport -level solutions
A major issue in all solutions is setting up the comm. paths 
for information dissemination ;  a huge management effort 
is involved, human intervention is required in many cases
With the advent of P2P technology , and notably 
structured overlay management, it becomes easier 
to set up comm. paths ;  as P2P solutions are typically 
deployed at the application layer, various application -
level multicasting techniques have been introduced
Distributed Systems 46
Multicast Communication (2)
Application -level multicasting
Basic idea: nodes are organized into an overlay network , 
which is then used to disseminate info to its members
Network routers are not involved in group membership;  
consequently, the connections between nodes in the 
overlay network may cross several physical links, and as 
such, routing messages may not be optimal
Two approaches in the construction of the overlay network
Nodes may organize themselves directly into a tree , meaning that 
there is a unique (overlay) path between every pair of nodes
Nodes may organize into a mesh network , in which every node will 
have multiple neighbors and, in general, there exist multiple paths 
between every pair of nodes
The latter provides higher robustness
Distributed Systems 47
Multicast Communication (3)
Application -level  ulticastin  (cont’d)
Building a tree is not difficult once we have organized the 
nodes into an overlay, but building an efficient tree may be 
a different story
The figure shows a set of five nodes organized in a simple 
overlay network ;  node Ais the root of a multicast tree
Whenever Amulticasts a msg to 
the other nodes, the msg will 
traverse links < B, Rb>, <Ra, Rb>, 
<E, Re>, <Rc, Rd>, <D, Rd> twice
The overlay network would have 
been more efficient if we had not 
constructed overlay links < B, E> & 
<D, E>, but instead < A, E> & < C, E> 
Distributed Systems 48

Multicast Communication (4)
Application -level  ulticastin  (cont’d)
The quality of an application -level multicast tree is 
generally measured by three different metrics :
Link stress →counts how often a packet crosses the same link
(when it is greater than 1, it means a packet may be forwarded 
along two different connections at a logical level, but part of those 
connections may actually correspond to the same physical link)
Stretch or Relative Delay Penalty (RDP) →measures the ratio of 
the delay between two nodes in the overlay against the delay that 
those two nodes would experience in the underlying network
(when constructing an overlay network, the goal is to minimize the 
aggregated stretch or the avg RDP measured over all node pairs)
Tree cost →a global metric related to minimizing the aggregated 
link costs (e.g., if the cost is taken to be the delay, then optimizing 
the tree cost boils down to finding a minimal spanning tree in 
which the total time for disseminating info to all nodes is minimal)
Distributed Systems 49
Multicast Communication (5)
Application -level  ulticastin  (cont’d)
Switch -trees solution
Assume we have a multicast tree with a single source as root
In this tree, a node Pcan switch parents by dropping the link to its 
current parent in favor of a link to another node ;  constraints are:
The new parent can never be a member of the subtree rooted at P
(as this would partition the tree and create a loop)
The new parent will not have too many immediate children (to limit 
the load of forwarding messages by any single node)
Different criteria for deciding to switch parents :
Optimizing the route to the source;  to this end, each node regularly 
receives info on other nodes so it can evaluate whether another 
node would be a better parent
The delay to the potential other parent is lower than to the current 
parent;  this simple scheme is a reasonable heuristic leading to a 
good approximation of a minimal spanning tree
Distributed Systems 50
Multicast Communication (6)
Application -level  ulticastin  (cont’d)
Switch -trees solution (cont’d)
For an example:
Node Preceives info on the neighbors of its parent;  the neighbors 
consists of P’s  rand arent and the other siblin s of P’s  arent
Node Pcan then evaluate the delays to each of these nodes and 
choose the one with the lowest delay, say Q, as its new parent;  
to that end, it sends a switch request to Q
To prevent loops from being formed due to concurrent switching 
requests, a node that has an outstanding switch request will simply 
refuse to process any incoming requests;  in effect, only completely 
independent switches can be carried out simultaneously
Whenever a node notices that its parent has failed , it simply 
attaches itself to the root ;  at that point, the optimization protocol 
can proceed as usual and will eventually place the node at a good 
point in the multicast tree
Distributed Systems 51
Multicast Communication (7)
Flooding -based multicasting 
Psimply sends a message 
mto each of its neighbors
Each neighbor will forward 
that message, except to P, 
and only if it had not seen 
mbefore
Variation ( probabilistic broadcasting ): Let Qforward a 
message with a probability Pflood, possibly even dependent 
on its own number of neighbors (i.e., node degree) or the 
degree of its neighbors 
In a random network of 10,000 nodes and Pedge= 0.1, we need only 
set Pflood= 0.01 to establish a more than 50 -fold reduction in the 
number of messages sent in comparison to full flooding 
Distributed Systems 52

Multicast Communication (8)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay (i.e., deterministic 
topology), designing efficient flooding schemes is simpler
Consider a 4 -dimensional hypercube 
A simple and efficient broadcast 
scheme relies on keeping track of 
neighbors per dimension
A node initially broadcasts a message 
mto all of its neighbors and tags m
with the label (i.e., dimension) of the 
edge over which it sends the message 
For example: If node 1001 broadcasts a message m, it will send ( m,1) 
to 0001, ( m,2) to 1101, ( m,3) to 1011, ( m,4) to 1000. When a node 
receives a broadcast message, it will forward it only along edges with 
a higher dimension. So, node 1101 will send ( m,3) to 1111 and ( m,4) 
to 1100. It can be shown that every broadcast requires precisely N−  
messages (where N= 2n= the no. of nodes in an n-dim hypercube) 
Distributed Systems 53

Multicast Communication (9)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay … (cont’d) 
Consider a 5 -bit Chord 
Assume that node 9 wants to flood a 
message to all other nodes 
Node 9 divides the ID space into four 
segments (one for each of its neighbors): 
node    ta es care of nodes ID    ≤ k< 14, 
node    for    ≤ k< 18, node 18 for 
   ≤ k<   , and node    for    ≤ k< 9 
Node 28 will subsequently divide the part 
of the ID space it is requested to handle 
into two subsegments: [1,4) and [4,9) 
Node 18 will split its segment into only one 
part and forward the message to [20,28) 
Lastly, node 20 forwards the message to 
[21,28) 
Distributed Systems 54

Multicast Communication (10)
Gossip -based data dissemination
An increasingly important technique for disseminating info
is to rely on epidemic behavior ;  epidemics studies the 
spreading of infectious diseases
The main goal is to rapidly propagate info among a large 
collection of nodes using only local info;  there is no central 
component by which info dissemination is coordinated
Using the terminology from epidemics:
A node that is part of a DS is called infected if it holds data that it is 
willing to spread to other nodes
A node that has not yet seen this data is called susceptible
An updated node that is not willing or able to spread its data is 
said to be removed
Distributed Systems 55
Multicast Communication (11)
Gossip -based data disse ination (cont’d)
We can distinguish old from new data, e.g., because it has 
been timestamped or versioned
A popular propagation model is that of anti-entropy ;  in 
this model, a node Ppicks another node Qat random, and 
subsequently exchanges updates with Qusing one of these 
three approaches :
Ponly pushes its own updates to Q
Ponly pulls in new updates from Q
Pand Qsend updates to each other (i.e., a push -pull approach)
When it comes to rapidly spreading updates, only pushing 
updates turns out to be a bad choice ;  if many nodes are 
infected, the probability of one selecting a susceptible 
node is relatively small
Distributed Systems 56
Multicast Communication (12)
Gossip -based data disse ination (cont’d)
The pull -based approach works much better when many 
nodes are infected ;  chances are big that a susceptible 
node will contact an infected one to subsequently pull in 
the updates and become infected as well
If only a single node is infected, updates will rapidly spread 
across all nodes using either form of anti -entropy, although 
push -pull remains the best strategy
Propagating a single update to all nodes takes 𝒪(log(N)) 
rounds, where Nis the number of nodes;  this indicates 
that propagating updates is fast, but above all scalable
One special variant of this approach is called rumor 
spreading , or simply gossiping
Distributed Systems 57
Multicast Communication (13)
Gossip -based data disse ination (cont’d)
Gossiping
If node Phas just been updated for data 
item x, it contacts an arbitrary other node 
Qand tries to push the update to Q
However, it is possible that Qwas already 
updated by another node;  in that case, P
may lose interest in spreading the update 
any further (with probability pstop), it then becomes removed
It is an excellent way of rapidly spreading news ;  however, it 
cannot guarantee that all nodes will actually be updated
One of the main advantages of epidemic algorithms is 
their scalability , due to the fact that the number of sync. 
between processes is relatively small compared to other 
propagation methods
Distributed Systems 58

Multicast Communication (14)
Gossip -based data disse ination (cont’d)
For wide -area systems, it makes sense to take the actual 
network topology into account to achieve better results
Nodes that are connected to only a few other nodes are contacted 
with a relatively high probability 
Assumption: such nodes form a bridge to other remote parts of 
network;  therefore, they should be contacted as soon as possible
This approach is referred to as directional gossiping
Most epidemic solutions assume that a node can randomly 
select any other node to gossip with
This implies that, in principle, the complete set of nodes should be 
known to each member;  in a large system, this can never hold
Fortunately, maintaining a partial view that is more or less 
continuously updated will organize the collection of nodes into a 
random graphDistributed Systems 59
Multicast Communication (15)
Gossip -based data disse ination (cont’d)
Epidemic algorithms have a rather strange side -effect: 
spreading the deletion of a data item is hard
The problem lies in the fact that deletion of a data item destroys 
all info on that item
Consequently, when a data item is simply removed from a node, 
the node will eventually receive old copies of the data item and 
interpret those as updates on something it did not have before
The trick is to record the deletion of a data item as just 
another update and keep a record of that deletion
In this way, old copies will not be interpreted as something new, 
but merely treated as versions that have been updated by a delete 
operation
The recording of a deletion is done by spreading death certificates
Distributed Systems 60
Multicast Communication (16)
Gossip -based data disse ination (cont’d)
The problem with death certificates is that they should 
eventually be cleaned up , or otherwise each node will 
gradually build a huge local database of historical info on 
deleted data items that actually are not used
Dormant death certificates
Each death cert is timestamped when it is created
If it can be assumed that updates propagate to all nodes within a 
known finite time, then death certs can be removed after this max 
propagation time has elapsed
To provide hard guarantees that deletions are indeed spread to all 
nodes, only a few nodes maintain dormant death certs that are 
never thrown away
Distributed Systems 61
RESERVED MATERIALS
Distributed Systems
Stream -Oriented Communication (1)
Communication as discussed so far has concentrated 
on exchanging more -or-less independent and 
complete units of information
There are forms of comm. in which timing plays a 
crucial role, e.g., an audio stream built up as a 
sequence of 16 -bit samples
Assume that the audio stream represents CD quality, 
meaning that the original sound wave has been sampled at 
a frequency of 44,100 Hz
To reproduce the original sound, it is essential that the 
samples in the audio stream are played out in the order 
they appear in the stream, but also at intervals of exactly 
1 / 44,100 second
Distributed Systems
Stream -Oriented Communication (2)
Support for the exchange of time -dependent info is 
often formulated as support for continuous media
In continuous (representation) media, the temporal 
relationships between different data items are 
fundamental to correctly interpreting what the data 
actually mean , e.g., an audio or video stream
In discrete (representation) media, the temporal 
relationships between data items are not
fundamental to correctly interpreting the data, e.g., 
text, still images, object code or executable files
Distributed Systems
Stream -Oriented Communication (3)
To capture the exchange of time -dependent info, 
DSes generally provide support for data streams
A data stream is a sequence of data units
It can be applied to discrete as well as continuous media
UNIX pipes or TCP/IP connections are typical examples of 
(byte -oriented) discrete data streams
Playing an audio file typically requires setting up a 
continuous data stream between the file and the audio 
device
To capture timing aspects, a distinction is often made 
between different transmission modes: 
asynchronous , synchronous , and isochronous
Distributed Systems
Stream -Oriented Communication (4)
Asynchronous transmission mode
The data items in a stream are transmitted one after the 
other, but there are no further timing constraints on when 
transmission of items should take place
This is typically the case for discrete data streams
Synchronous transmission mode
There is a maximum end -to-end delay defined for each 
unit in a data stream
It may be important that the end -to-end propagation time 
through the network is guaranteed to be lower that the 
time interval between taking samples, but it cannot do any 
harm if samples are propagated faster than necessary
E.g., a sensor sending sample temperature at a certain rate
Distributed Systems
Stream -Oriented Communication (5)
Isochronous transmission mode
It is necessary that data units are transferred on time;  this 
means that data transfer is subject to a maximum and 
minimum end -to-end delay, also referred to as bounded 
(delay) jitter
It plays a crucial role in representing audio and video
Streams can be simple or complex
A simple stream consists of only a single sequence of data
A complex stream consists of several related simple 
streams, called substreams ;  the relation between the 
substreams is often also time dependent
Distributed Systems
Stream -Oriented Communication (6)
From a DS perspective, we can distinguish several 
elements needed for supporting streams
For simplicity, we concentrate on streaming stored data, as 
opposed to streaming live data
We can sketch a general client -server architecture
Distributed Systems

Stream -Oriented Communication (7)
QoS ro erties fro  an a  lication’s  ers ective:
The required bit rate at which data should be transported
The max delay until a session has been set up (i.e., when 
an application can start sending data) 
The max end -to-end delay (i.e., how long it will take until a 
data unit makes it to a recipient)
The max delay variance, or jitter
The max round -trip delay
When dealing with stream -oriented comm. that is 
based on the Internet protocol stack, the basis of 
comm. is formed by an extremely simple, best -effort 
datagram service (i.e., IP) 
Distributed Systems
Stream -Oriented Communication (8)
Given that the underlying system offers only a best -
effort delivery service, a DS can try to conceal as 
much as possible of the lack of QoS
The Internet provides a means for differentiated services;  
a sending host can essentially mark outgoing packets as 
belonging to one of several classes, including an expedited 
forwarding class and an assured forwarding class (by which 
traffic is divided into four subclasses along with three ways 
to drop packets if the network gets congested)
DS may use buffers to 
reduce jitter
Distributed Systems

Stream -Oriented Communication (9)
Given that … (cont’d)
Applying forward error correction (FEC) techniques to 
compensate for the loss in QoS
Since a single packet may contain multiple audio and video 
frames, when it is lost, the receiver may actually perceive a 
large gap when playing out frames;  this can be somewhat 
circumvented by interleaving frames, but this approach 
requires a large receive buffer and thus imposes a higher 
start delay for the receiving application
Distributed Systems

Stream -Oriented Communication (10)
Stream synchronization
Synchronization of streams deals with maintaining 
temporal relations between streams
Sync. between a discrete data stream & a continuous data stream, 
e.g., a slide show enhanced with audio
Sync. between continuous data streams, e.g., a video stream 
synchronized with the audio (lip synchronization), a stereo audio 
stream consisting two substreams
Two issues in stream synchronization:
The basic mechanisms for synchronizing two streams
The distribution of those mechanisms in a networked environment
Sync. mechanisms can be viewed at several different levels 
of abstraction
Distributed Systems
Stream -Oriented Communication (11)
Strea  synchronization (cont’d)
At the lowest level, sync. is done explicitly by operating on 
the data units of simple streams
There is a process that simply executes read and write operations 
on several simple streams, ensuring that those operations adhere 
to specific timing and sync. constraints
Consider a movie presented as 
2 input streams (video & audio)
The video stream contains 
uncompressed low -quality 
images of 320 240 pixels, each 
encoded by a single byte, 
leading to video data units of 
76,800 bytes each;  the images 
are to be displayed at 30 Hz, or 
one image every 33 ms
Distributed Systems

Stream -Oriented Communication (12)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
Consider a  ovie … (cont’d)
The 44.1 kHz, 16 -bit, stereo audio stream contains samples grouped 
into units of 5,880 bytes, each corresponding to 33 ms of audio
If the input process can handle 2.5 Mbps, we can achieve lip sync. by 
simply alternating between reading an image and reading a block of 
audio samples every 33 ms;  the drawback of this approach is that the 
application is made completely responsible for implementing sync. 
while it has only low -level facilities available
A better approach is to offer an interface that allows the 
application to more easily control streams and devices
An application developer can write a simple monitor program 
consisting of two handlers, one for each stream, that jointly check if 
the video and audio streams are sufficiently synchronized, and if 
needed, adjust the rate at which video or audio units are presented
Distributed Systems
Stream -Oriented Communication (13)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
The last example is typical for multimedia middleware systems
The middleware offers a collection of interfaces for controlling 
audio and video streams, including interfaces for controlling 
devices, e.g., monitors, cameras, microphones, etc.
Each device and stream has 
its own high -level interfaces, 
including interfaces for 
notifying an application 
when some event occurred;  
the latter interfaces are 
subsequently used to write 
handlers for synchronizing 
streams
Distributed Systems

Stream -Oriented Communication (14)
Strea  synchronization (cont’d)
The distribution of synchronization mechanisms
The receiving side of a complex stream needs to know exactly 
what to do;  it must have a complete synchronization specification
locally available
Common practice is to provide this info implicitly by multiplexing the 
different streams into a single stream containing all data units, 
including those for sync.
For an example: the MPEG -2 standard allows an unlimited number of 
continuous and discrete streams to be merged into a single stream
Another issue is whether sync. should take place at the sending or 
receiving side
If the sender handles sync., it may merge streams into a single 
stream with a different type of data units, e.g., a stereo audio stream
The receiver merely has to read in a data unit, and split it into a left 
and right sample;  delays for both channels are now identical
Distributed Systems
Distributed Systems 
Communication 
Lecture 04

Fundamentals (1)
Interprocess communication is at the heart of all DSes
Due to the absence of shared memory, all 
communication in DSes is based on sending and 
receiving (low level) messages
Communication through message passing is harder 
than using primitives based on shared memory
Modern DSes often consist of thousands or even millions of 
processes scattered across an unreliable network
Many different agreements (e.g., protocols) are needed 
between the communicating parties, varying from the low -
level details of bit transmission to the high -level details of 
how information is to be expressed
Distributed Systems 2

Fundamentals (2)
Basic networking model
For many DSes , the lowest -level interface is that of the 
network layer
Distributed Systems 3


Fundamentals (3)
Transport Layer: provides the actual communication 
facilities for most DSes
TCP: connection -oriented, reliable, stream -oriented 
communication 
UDP: unreliable (best -effort) datagram communication 
RTP (Real -time Transport Protocol): specifies packet 
formats for real -time data without providing the actual 
mechanisms for guaranteeing data delivery, and specifies a 
protocol for monitoring and controlling data transfer 
SCTP (Streaming Control Transmission Protocol): groups 
data into messages (i.e., an alternative to TCP that merely 
moves bytes between processes) 
Distributed Systems 4

Fundamentals (4)
Middleware protocols: provide common services and 
protocols that can be used by many different apps
A rich set of 
communication protocols
(Un)marshaling of data, 
necessary for integrated 
systems 
Naming protocols to allow 
easy sharing of resources 
Security protocols for 
secure communication 
Scaling mechanisms , such 
as for replication & caching 
Distributed Systems 5
Adapted reference model 
for networked communication 

Fundamentals (5)
Types of communication
Persistent communication →the message that has been 
submitted for transmission is stored by the communication 
middleware as long as it takes to deliver it to the receiver
The sending application need not continue execution after 
submitting the message
The receiving application need not be executing when the 
message is submitted
Transient communication →the message is stored by the 
communication system only as long as the sending and 
receiving applications are executing
The communication system consists of traditional store -and-
forward routers
If it cannot deliver a message, it will simply drop the message
Distributed Systems 6

Fundamentals (6)
Types of communication (cont’d)
Asynchronous communication →the sender continues 
immediately after it has submitted its message for 
transmission
Synchronous communication →the sender is blocked until 
its request is known to be accepted
The sender may be blocked until the middleware notifies that it 
will take over transmission of the request
The sender may synchronize until its request has been delivered to 
the intended recipient
The sender may wait until its request has been fully processed, 
i.e., up to the time that the recipient returns a response
Various combinations of persistence and synchronization 
occur in practice, e.g., message -queuing systems, RPCs
Distributed Systems 7

Fundamentals (7)
Types of communication (cont’d) 
Distributed Systems 8


Fundamentals (8)
Types of communication (cont’d)
Discrete communication →the parties communicate by 
messages, each of which forms a complete unit of 
information
Streaming communication →sending multiple messages, 
one after another, where the messages are related to each 
other by the order they are sent, or because there is a 
temporal relationship
Distributed Systems 9

Remote Procedure Call (1)
Many DSes have been based on explicit message 
exchange between processes ;  however, the send and 
receive do not conceal communication at all (i.e., no 
access transparency)
Birrell and Nelson [1984] suggested to allow programs 
to call procedures located on other machines ;  this 
method is known as Remote Procedure Call (RPC)
The basic idea sounds simple and elegant, but subtle 
problems exist
They execute in different address space, and parameters & 
results have to be passed, which can be complicated if the 
machines are not identical
Either or both machines can crash & cause more problems
Distributed Systems 10

Remote Procedure Call (2)
Conventional procedure call
Consider operation newlist = append(data, dbList);
The purpose is to take a globally defined list object (i.e., 
dbList ) and append a single data element to it (i.e., data ) 
In various programming languages, dbList is a reference to 
a list object, whereas data may be represented by its value 
When calling append , both the 
representations of data and 
dbList are pushed onto the 
stack, making them accessible to 
the implementation of append
Variable data follows a call-by-
value policy and variable dbList
a call-by-reference
Distributed Systems 11


Remote Procedure Call (3)
Conventional procedure call (cont’d)
A value parameter is just an initialized local variable;  the 
called procedure may modify it, but do not affect the 
original at the calling side 
A reference parameter is a pointer to a variable, so the 
address of the variable as stored in main memory is pushed 
onto the stack;  when a call to append adds the value of 
data to dbList , the list object in main memory is modified 
The difference between call -by-value and call -by-reference 
is quite important for RPC
The decision of which parameter passing mechanism to use 
is made by the language designers & a fixed property of the 
language
Distributed Systems 12

Remote Procedure Call (4)
Client and server stubs
The idea behind RPC is to make it look as much as possible 
like a local one ;  i.e., make it transparent –the calling 
procedure should not be aware that the called procedure 
is executing on a different machine or vice versa
When append is actually a remote procedure, a different 
version of append–called a client stub –is offered
It is called using the normal calling 
sequence like the original one
It does not perform an append
operation; instead, it packs the 
parameters into a message and 
requests that message to be sent 
to the remote server
Following the call to send , the client stub calls receive , blocking 
itself until the reply comes back
Distributed Systems 13


Remote Procedure Call (5)
Client and server stubs (cont’d)
When the message arrives at the server , the server’s OS 
passes it up to a server stub (i.e., the server -side equivalent 
of a client stub)
Typically the server stub will have called receive and be blocked 
waiting for incoming messages 
It transforms requests coming in over the network into local 
procedure calls 
The server performs its work and returns the result to the caller 
(i.e., server stub) 
When the server stub gets control back, it packs the result in a 
message and calls send to return it to the client 
After that, the server stub usually does a call to receive again 
When the message arrives at the client machine , the OS 
passes it to the client stub , which returns it to the caller 
Distributed Systems 14

Remote Procedure Call (6)
Client and server stubs (cont’d)
Distributed Systems 15
  Client  rocedure calls client stub  
  Stub builds  essa e calls local OS 
  OS sends  essa e to re ote OS  
   e ote OS  ives  essa e to stub  
  Stub un ac s  ara eter s calls server   Server does local call returns result to stub  
  Stub builds  essa e  calls OS 
  OS sends  essa e to client  s OS 
  Client s OS  ives  essa e to stub  
   Client stub un ac s result  returns to client 

Remote Procedure Call (7)
Parameter passing
Packing parameters into a message is called parameter 
marshaling
There is more than just wrapping parameters into a message 
Client and server machines may have different data representations
(i.e., byte ordering –little vs. big endian) 
Wrapping a parameter means transforming a value into a sequence 
of bytes
Client and server have to agree on the same encoding : 
How are basic data values represented (integers, floats, characters) 
How are complex data values represented (arrays, unions) 
Both need to properly interpret messages →transforming them into 
machine -independent representations
Distributed Systems 16

Remote Procedure Call (8)
Para eter  assin  (cont’d)
How are pointers, or in general, references passed ?
One solution is to forbid pointers & reference params in general
Another strategy is to copy the array (according to its size) into the 
message and send it to the server;  in effect, call -by-reference has 
been replaced by call -by-copy/restore
When the client stub knows the referred data will be only read, 
there is no need to copy it back when the call has finished 
Using global references (i.e., meaningful to the calling and the 
called processes);  e.g., if the client and the server have access to 
the same file system, a file handle (instead of a pointer) is passed 
Distributed Systems 17

Remote Procedure Call (9)
Variations on RPC: Asynchronous RPC
The server immediately sends a reply back to the client the 
moment the RPC request is received ;  the reply acts as an 
acknowledgement to the client
The client will continue without further blocking as soon as 
it has received the server’s ac nowled e ent
Deferred synchronous RPC
→combining an async RPC 
with a callback 
One-way RPC→client 
does not wait for an ack 
Distributed Systems 18


Remote Procedure Call (10)
Variations on RPC: Multicast RPC
Executing multiple RPCs at the same time →adopting the 
one-way RPCs to send an RPC request to a group of servers 
Issues to consider : 
The client app may be unaware 
that an RPC is actually being
forwarded to multiple servers 
(e.g., to increase fault tolerance, 
have all operations executed by 
a backup server who can take 
over when the main server fails) 
Will the client proceed after all 
responses have been received, 
or wait just for one?  It depends 
whether the server has been replicated for fault tolerance or to do 
the same work but on different parts of the input 
Distributed Systems 19


Message -Oriented Communication
RPC and remote object invocations are not always 
appropriate, particularly when it cannot be assumed 
that the receiving side is executing at the time a 
request is issued
Messaging or message -oriented communication is an 
alternative communication service to RPCs
Two types of message -oriented communication:
Message -oriented transient communication
Message -oriented persistent communication
Distributed Systems 20

Msg -Oriented Transient Comm. (1)
Many distributed systems and applications are built 
directly on top of the simple message -oriented 
model offered by the transport layer
Standard interfaces have been introduced to the 
transport layer to allow programmers to make use of 
its entire suite of (messaging) protocols through a 
simple set of operations
The standard interfaces also make it easier to port an 
application to a different machine
An example is the sockets interface introduced in the 
1970s in Berkeley UNIX, known as Berkeley Sockets
Distributed Systems 21

Msg -Oriented Transient Comm. (2)
Berkeley sockets
Conceptually, a socket is a communication end point to 
which an application can write data that are to be sent out 
over the underlying network, and from which incoming 
data can be read
A socket forms an abstraction over the actual port that is 
used by the local OS for a specific transport protocol (e.g., 
TCP)
Servers generally execute the first four operations (i.e., 
socket , bind , listen , and accept ), normally in the order 
given
Distributed Systems 22

Msg -Oriented Transient Comm. (3)
Ber eley soc ets (cont’d)
When calling the socket operation , the caller creates a new 
comm. end point for a specific transport protocol
Internally, it means that the local OS reserves resources to 
accommodate sending and receiving messages for the specified 
protocol
The bind operation associates a local address with the 
newly -created socket , e.g., a server should bind the IP 
address of its machine together with a (possibly well -
known) port number to a socket
Binding tells the OS that the server wants to receive messages only 
on the specified address and port
Distributed Systems 23

Msg -Oriented Transient Comm. (4)
Ber eley soc ets (cont’d)
The listen operation is called only in the case of 
connection -oriented communication
It is a non -blocking call that allows the local OS to reserve enough 
buffers for a specified maximum number of pending connection 
requests that the caller is willing to accept
A call to accept blocks the caller until a connection request 
arrives
When a request arrives, the local OS creates a new socket with the 
same properties as the original one, and returns it to the caller
This approach will allow the server to, for example, fork a process 
that will subsequently handle the actual comm. through the new 
connection;  the server, in the meantime, can go back and wait for 
another connection request on the original socket
Distributed Systems 24

Msg -Oriented Transient Comm. (5)
Ber eley soc ets (cont’d)
At the client side , the order of execution is as the following
A socket must first be created using the socket operation, but 
explicitly binding the socket to a local address is not necessary, 
since the OS can dynamically allocate a port when the connection 
is set up
The connect operation requires that the caller specifies the 
transport -level address to which a connection request is to be 
sent;  the client is blocked until a connection has been set up 
successfully
After that, both sides can start exchanging information through 
the send and receive operations
Finally, closing a connection is symmetric when using sockets, and 
is established by having both the client and server call the close
operation
Distributed Systems 25

Msg -Oriented Transient Comm. (6)
Ber eley soc ets (cont’d)
Distributed Systems 26
                    
      
    
      
      
       
    
       
                                         
                                
                                                        
                             
                                          
                                          
                                  
                                     
                      


Msg -Oriented Transient Comm. (7)
Sockets are rather low level and programming 
mistakes are easily made
More advanced approaches for msg -oriented comm. 
is needed to: 
make network programming easier 
expand beyond the functionality offered by existing 
networking protocols 
make better use of local resources 
etc. 
Distributed Systems 27

Msg -Oriented Transient Comm. (8)
ZeroMQ
Provides a higher level of expression by pairing sockets : 
one for sending messages and a corresponding one for 
receiving messages 
Supports many -to-one and one-to-many communication
All communication is asynchronous
Three communication patterns supported: 
Request -reply–used intraditional client -server communication
Publish -subscribe –clients subscribe to specific messages that are 
published by servers
Pipeline–a process wants to push out its results , assuming that 
there are other processes that want to pull in those results
Distributed Systems 28

Msg -Oriented Transient Comm. (9)
Sockets were deemed insufficient for communication 
in high -performance multicomputers :
They were at the wrong level of abstraction by supporting 
only simple send and receive operations 
Sockets had been designed to communicate across networks 
using general -purpose protocol stacks (e.g., TCP/IP), not 
suitable for the proprietary protocols for high -speed 
interconnection networks
The need to be hardware and software independent 
eventually led to the definition of a standard called the 
Message -Passing Interface (MPI)
Designed for parallel apps and tailored to transient comm.
Make direct use of the underlying network
Assume that serious failures do not require auto recovery
Distributed Systems 29

Msg -Oriented Transient Comm. (10)
Message -Passing Interface
MPI assumes that comm. takes place within a known 
group of processes ;  each group is assigned an identifier, 
and each process within a group is also assigned a (local) id
A (groupID , processID ) pair uniquely identifies the source 
or destination of a message , and is used instead of a 
transport -level address
There may be several, overlapping groups of processes 
involved in a computation and that are all executing at the 
same time
At the core of MPI are messaging operations to support 
transient comm. , of which the most intuitive ones are 
discussed in the following slides
Distributed Systems 30

Msg -Oriented Transient Comm. (11)
Message -Passing Interface (cont’d)
The MPI_SEND operation –which is implementation 
dependent –is a blocking send operation that may block 
the caller either until the specified message has been 
co ied to the MPI runti e syste  at the sender’s side, or 
until the receiver has initiated a receive operation
The MPI_BSEND operation supports transient async comm.
The sender submits a message for transmission, which is generally 
first copied to a local buffer in the MPI runtime system
When the message has been copied, the sender continues
The local MPI runtime system will remove the message from its 
local buffer and take care of transmission as soon as a receiver has 
called a receive primitive
The MPI_SSEND operation is sync comm. by which the 
sender blocks until its request is accepted for further 
processing
Distributed Systems 31

Msg -Oriented Transient Comm. (12)
Message -Passing Interface (cont’d)
The MPI_SENDRECV operation gives the strongest form of 
sync comm. , in which it sends a request to the receiver and 
blocks until the latter returns a reply ;  basically, it 
corresponds to a normal RPC
The MPI_ISEND operation is a variant of MPI_SEND that 
supports async comm., in which the sender passes a 
pointer to the message (i.e., avoiding copying messages 
from user buffers to buffers internal to the local MPI 
runtime system) and immediately continues
Likewise, the MPI_ISSEND operation is the async variant of 
MPI_SSEND , in which the sender  asses only a  essa e’s 
pointer to the MPI runtime system and continues after the 
runtime system indicates it has processed the message
Distributed Systems 32

Msg -Oriented Transient Comm. (13)
Message -Passing Interface (cont’d)
The MPI_RECV operation is called to receive a message ;  
it blocks the caller until a message arrives
The MPI_IRECV operation is the async variant , by which a 
receiver indicates that it is prepared to accept a message
Distributed Systems 33
                    
                                                       
                                                                      
                                                          
                                             
                                                         
                                                                           
                                                 
                                                                

Msg -Oriented Persistent Comm. (1)
Message -queuing systems , often called Message -
Oriented Middleware (MOM) , provide extensive 
support for persistent async comm.
They offer intermediate -term storage capacity for messages , 
without requiring either the sender or receiver to be active 
during message transmission
They are typically targeted to support message transfers 
that are allowed to take minutes instead of seconds or 
milliseconds
The basic idea is that applications communicate by 
inserting messages in specific queues
The messages are forwarded over a series of comm. 
servers and are eventually delivered to the destination 
(which could be down)
Distributed Systems 34

Msg -Oriented Persistent Comm. (2)
In practice, most comm. servers are directly connected 
to each other ;  so, a message is generally transferred 
directly to a destination server
In principle, each application has its own private queue
to which other applications can send messages;  the 
queue can be read only by its associated application, 
but it is also possible for multiple applications to share 
a single queue
A sender is generally given only the guarantees that its 
 essa e will eventually be inserted in the reci ient’s 
queue ;  no guarantees about when, or even if the 
message will actually be read
The sender & receiver can execute independently
Distributed Systems 35

Msg -Oriented Persistent Comm. (3)
Four combinations for loosely coupled communication
Distributed Systems 36


Msg -Oriented Persistent Comm. (4)
The only important aspect from the perspective of 
middleware is that messages are properly addressed
Addressing is done by providing a system -wide unique 
name of the destination queue
Message size may be limited in some cases, although it is 
also possible that the underlying system takes care of 
fragmenting and assembling large messages in a way that 
is completely transparent to applications
The PUT operation is a nonblocking call called by a 
sender to pass a message to the underlying system 
that is to be appended to the specified queue
The GET operation is a blocking call by which an 
authorized process can remove the longest pending 
message in the specified queue
Distributed Systems 37

Msg -Oriented Persistent Comm. (5)
Variations of the GET call allow searching for a 
specific message in the queue , e.g., using a priority 
or a matching pattern
The nonblocking variant is given by the POLL
operation, which simply continues if the queue is 
empty or if a specific message could not be found
Most queuing systems also allow a process to install 
a handler as a callback function (through a NOTIFY
operation), automatically invoked whenever a 
message is put into the queue
Callbacks can also be used to automatically start a process –if 
none is executing –that will fetch messages from the queue
Often implemented by means of a daemon that monitors the 
queue for incoming messages and handles accordingly
Distributed Systems 38

Msg -Oriented Persistent Comm. (6)
It is the responsibility of a message -queuing system
to provide queues to senders & receivers and take 
care that messages are transferred from their source 
to their destination queue
The collection of queues is distributed across 
multiple machines ;  thus, a message -queuing system 
should maintain a (possibly distributed) database 
that maps queue names to network locations
Distributed Systems 39
                    
                                  
                                                                  
                                                                 
                                                                      

Msg -Oriented Persistent Comm. (7)
Queues are managed by queue managers
Normally, a queue manager interacts directly with the 
application that is sending or receiving a message
Some special queue managers operate as routers or relays
as they forward incoming messages to other managers
A message -queuing system may gradually grow into a 
complete, application -level, overlay network
Distributed Systems 40


Msg -Oriented Persistent Comm. (8)
An important application area of message -queuing 
systems is integrating existing and new applications 
into a single, coherent distributed system
It requires that applications can understand the messages 
they receive ;  it requires the sender to have its outgoing 
messages in the same format as that of the receiver
The problem is that each time an application requiring a 
separate messaging protocol is added to the system, other 
application communicating with it will need to provide the 
means for converting their respective messages
An alternative is to agree on a common messaging 
protocol ;  however, it makes sense only if the 
collection of processes that make use of that 
protocol indeed have enough in common
Distributed Systems 41

Msg -Oriented Persistent Comm. (9)
The general approach is to learn to live with 
differences , and try to provide the means to make 
conversions as simple as possible
Conversions are handled by message brokers
A message broker acts as an application -level gateway in a 
message -queuing system;  a message broker is generally 
not considered an integral part of the queuing system
It can be as simple as a reformatter for messages , e.g., 
changing record delimiters and field formats
It may handle conversion between two different database 
applications
More common is its use for advanced enterprise 
application integration (EAI) , like matching apps based on 
the messages being exchanged (i.e., pub -sub model) 
Distributed Systems 42

Msg -Oriented Persistent Comm. (10)
At the heart of a message broker lies a repository of 
rules for transforming a message of one type to 
another;  the problem is defining the rules and 
developing the plugins
Distributed Systems 43


Example: AMQP (1)
Advanced Message -Queuing Protocol was intended to play 
the same role as, e.g., TCP in networks: a protocol for high -
level messaging with different implementations
Implementations of 
AMQP: RabbitMQ & 
A ache’s ActiveMQ 
AMQP revolves 
around applications, 
queue managers, 
and queues
Basic model: 
App sets up a connection (i.e., a container for a number of one-way 
channels ) to a queue manager ;  two one -way channels form a session
A linkis akin to a socket and maintains state about message transfers
Distributed Systems 44


Example: AMQP (2)
When a message is to be transferred, the app passes it to local 
AMQP stub;  message transfer normally proceeds in 3 steps : 
At the sender’s side, the message is assigned a unique ID and is 
recorded locally to be in an unsettled state . The stub subsequently 
transfers the message to the server , where the AMQP stub also 
records it as being in an unsettled state. Then, the server -side stub 
passes it to the queue manager . 
The receiving app (i.e., queue manager) is assumed to handle the 
message and normally reports back to its stub that it is finished . The 
stub passes this info to the original sender , at which point the message 
at the ori inal sender’s AMQP stub enters a settled state . 
The AMQP stub of the original sender now tells the stub of the original 
receiver that message transfer has been settled (i.e., the original 
sender will for et about the  essa e fro  now on)  The receiver’s 
stub can now also discard anything about the message , formally 
recording it as being settled as well. 
Distributed Systems 45

Multicast Communication (1)
Multicast communication in DSes is the support for 
sending data to multiple receivers
For many years, this topic has belonged to the domain of 
network protocols;  some are network -level solutions and 
the others are transport -level solutions
A major issue in all solutions is setting up the comm. paths 
for information dissemination ;  a huge management effort 
is involved, human intervention is required in many cases
With the advent of P2P technology , and notably 
structured overlay management, it becomes easier 
to set up comm. paths ;  as P2P solutions are typically 
deployed at the application layer, various application -
level multicasting techniques have been introduced
Distributed Systems 46

Multicast Communication (2)
Application -level multicasting
Basic idea: nodes are organized into an overlay network , 
which is then used to disseminate info to its members
Network routers are not involved in group membership;  
consequently, the connections between nodes in the 
overlay network may cross several physical links, and as 
such, routing messages may not be optimal
Two approaches in the construction of the overlay network
Nodes may organize themselves directly into a tree , meaning that 
there is a unique (overlay) path between every pair of nodes
Nodes may organize into a mesh network , in which every node will 
have multiple neighbors and, in general, there exist multiple paths 
between every pair of nodes
The latter provides higher robustness
Distributed Systems 47

Multicast Communication (3)
Application -level  ulticastin  (cont’d)
Building a tree is not difficult once we have organized the 
nodes into an overlay, but building an efficient tree may be 
a different story
The figure shows a set of five nodes organized in a simple 
overlay network ;  node Ais the root of a multicast tree
Whenever Amulticasts a msg to 
the other nodes, the msg will 
traverse links < B, Rb>, <Ra, Rb>, 
<E, Re>, <Rc, Rd>, <D, Rd> twice
The overlay network would have 
been more efficient if we had not 
constructed overlay links < B, E> & 
<D, E>, but instead < A, E> & < C, E> 
Distributed Systems 48


Multicast Communication (4)
Application -level  ulticastin  (cont’d)
The quality of an application -level multicast tree is 
generally measured by three different metrics :
Link stress →counts how often a packet crosses the same link
(when it is greater than 1, it means a packet may be forwarded 
along two different connections at a logical level, but part of those 
connections may actually correspond to the same physical link)
Stretch or Relative Delay Penalty (RDP) →measures the ratio of 
the delay between two nodes in the overlay against the delay that 
those two nodes would experience in the underlying network
(when constructing an overlay network, the goal is to minimize the 
aggregated stretch or the avg RDP measured over all node pairs)
Tree cost →a global metric related to minimizing the aggregated 
link costs (e.g., if the cost is taken to be the delay, then optimizing 
the tree cost boils down to finding a minimal spanning tree in 
which the total time for disseminating info to all nodes is minimal)
Distributed Systems 49

Multicast Communication (5)
Application -level  ulticastin  (cont’d)
Switch -trees solution
Assume we have a multicast tree with a single source as root
In this tree, a node Pcan switch parents by dropping the link to its 
current parent in favor of a link to another node ;  constraints are:
The new parent can never be a member of the subtree rooted at P
(as this would partition the tree and create a loop)
The new parent will not have too many immediate children (to limit 
the load of forwarding messages by any single node)
Different criteria for deciding to switch parents :
Optimizing the route to the source;  to this end, each node regularly 
receives info on other nodes so it can evaluate whether another 
node would be a better parent
The delay to the potential other parent is lower than to the current 
parent;  this simple scheme is a reasonable heuristic leading to a 
good approximation of a minimal spanning tree
Distributed Systems 50

Multicast Communication (6)
Application -level  ulticastin  (cont’d)
Switch -trees solution (cont’d)
For an example:
Node Preceives info on the neighbors of its parent;  the neighbors 
consists of P’s  rand arent and the other siblin s of P’s  arent
Node Pcan then evaluate the delays to each of these nodes and 
choose the one with the lowest delay, say Q, as its new parent;  
to that end, it sends a switch request to Q
To prevent loops from being formed due to concurrent switching 
requests, a node that has an outstanding switch request will simply 
refuse to process any incoming requests;  in effect, only completely 
independent switches can be carried out simultaneously
Whenever a node notices that its parent has failed , it simply 
attaches itself to the root ;  at that point, the optimization protocol 
can proceed as usual and will eventually place the node at a good 
point in the multicast tree
Distributed Systems 51

Multicast Communication (7)
Flooding -based multicasting 
Psimply sends a message 
mto each of its neighbors
Each neighbor will forward 
that message, except to P, 
and only if it had not seen 
mbefore
Variation ( probabilistic broadcasting ): Let Qforward a 
message with a probability Pflood, possibly even dependent 
on its own number of neighbors (i.e., node degree) or the 
degree of its neighbors 
In a random network of 10,000 nodes and Pedge= 0.1, we need only 
set Pflood= 0.01 to establish a more than 50 -fold reduction in the 
number of messages sent in comparison to full flooding 
Distributed Systems 52


Multicast Communication (8)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay (i.e., deterministic 
topology), designing efficient flooding schemes is simpler
Consider a 4 -dimensional hypercube 
A simple and efficient broadcast 
scheme relies on keeping track of 
neighbors per dimension
A node initially broadcasts a message 
mto all of its neighbors and tags m
with the label (i.e., dimension) of the 
edge over which it sends the message 
For example: If node 1001 broadcasts a message m, it will send ( m,1) 
to 0001, ( m,2) to 1101, ( m,3) to 1011, ( m,4) to 1000. When a node 
receives a broadcast message, it will forward it only along edges with 
a higher dimension. So, node 1101 will send ( m,3) to 1111 and ( m,4) 
to 1100. It can be shown that every broadcast requires precisely N−  
messages (where N= 2n= the no. of nodes in an n-dim hypercube) 
Distributed Systems 53


Multicast Communication (9)
Flooding -based  ulticastin  (cont’d) 
When dealing with a structured overlay … (cont’d) 
Consider a 5 -bit Chord 
Assume that node 9 wants to flood a 
message to all other nodes 
Node 9 divides the ID space into four 
segments (one for each of its neighbors): 
node    ta es care of nodes ID    ≤ k< 14, 
node    for    ≤ k< 18, node 18 for 
   ≤ k<   , and node    for    ≤ k< 9 
Node 28 will subsequently divide the part 
of the ID space it is requested to handle 
into two subsegments: [1,4) and [4,9) 
Node 18 will split its segment into only one 
part and forward the message to [20,28) 
Lastly, node 20 forwards the message to 
[21,28) 
Distributed Systems 54


Multicast Communication (10)
Gossip -based data dissemination
An increasingly important technique for disseminating info
is to rely on epidemic behavior ;  epidemics studies the 
spreading of infectious diseases
The main goal is to rapidly propagate info among a large 
collection of nodes using only local info;  there is no central 
component by which info dissemination is coordinated
Using the terminology from epidemics:
A node that is part of a DS is called infected if it holds data that it is 
willing to spread to other nodes
A node that has not yet seen this data is called susceptible
An updated node that is not willing or able to spread its data is 
said to be removed
Distributed Systems 55

Multicast Communication (11)
Gossip -based data disse ination (cont’d)
We can distinguish old from new data, e.g., because it has 
been timestamped or versioned
A popular propagation model is that of anti-entropy ;  in 
this model, a node Ppicks another node Qat random, and 
subsequently exchanges updates with Qusing one of these 
three approaches :
Ponly pushes its own updates to Q
Ponly pulls in new updates from Q
Pand Qsend updates to each other (i.e., a push -pull approach)
When it comes to rapidly spreading updates, only pushing 
updates turns out to be a bad choice ;  if many nodes are 
infected, the probability of one selecting a susceptible 
node is relatively small
Distributed Systems 56

Multicast Communication (12)
Gossip -based data disse ination (cont’d)
The pull -based approach works much better when many 
nodes are infected ;  chances are big that a susceptible 
node will contact an infected one to subsequently pull in 
the updates and become infected as well
If only a single node is infected, updates will rapidly spread 
across all nodes using either form of anti -entropy, although 
push -pull remains the best strategy
Propagating a single update to all nodes takes 𝒪(log(N)) 
rounds, where Nis the number of nodes;  this indicates 
that propagating updates is fast, but above all scalable
One special variant of this approach is called rumor 
spreading , or simply gossiping
Distributed Systems 57

Multicast Communication (13)
Gossip -based data disse ination (cont’d)
Gossiping
If node Phas just been updated for data 
item x, it contacts an arbitrary other node 
Qand tries to push the update to Q
However, it is possible that Qwas already 
updated by another node;  in that case, P
may lose interest in spreading the update 
any further (with probability pstop), it then becomes removed
It is an excellent way of rapidly spreading news ;  however, it 
cannot guarantee that all nodes will actually be updated
One of the main advantages of epidemic algorithms is 
their scalability , due to the fact that the number of sync. 
between processes is relatively small compared to other 
propagation methods
Distributed Systems 58


Multicast Communication (14)
Gossip -based data disse ination (cont’d)
For wide -area systems, it makes sense to take the actual 
network topology into account to achieve better results
Nodes that are connected to only a few other nodes are contacted 
with a relatively high probability 
Assumption: such nodes form a bridge to other remote parts of 
network;  therefore, they should be contacted as soon as possible
This approach is referred to as directional gossiping
Most epidemic solutions assume that a node can randomly 
select any other node to gossip with
This implies that, in principle, the complete set of nodes should be 
known to each member;  in a large system, this can never hold
Fortunately, maintaining a partial view that is more or less 
continuously updated will organize the collection of nodes into a 
random graphDistributed Systems 59

Multicast Communication (15)
Gossip -based data disse ination (cont’d)
Epidemic algorithms have a rather strange side -effect: 
spreading the deletion of a data item is hard
The problem lies in the fact that deletion of a data item destroys 
all info on that item
Consequently, when a data item is simply removed from a node, 
the node will eventually receive old copies of the data item and 
interpret those as updates on something it did not have before
The trick is to record the deletion of a data item as just 
another update and keep a record of that deletion
In this way, old copies will not be interpreted as something new, 
but merely treated as versions that have been updated by a delete 
operation
The recording of a deletion is done by spreading death certificates
Distributed Systems 60

Multicast Communication (16)
Gossip -based data disse ination (cont’d)
The problem with death certificates is that they should 
eventually be cleaned up , or otherwise each node will 
gradually build a huge local database of historical info on 
deleted data items that actually are not used
Dormant death certificates
Each death cert is timestamped when it is created
If it can be assumed that updates propagate to all nodes within a 
known finite time, then death certs can be removed after this max 
propagation time has elapsed
To provide hard guarantees that deletions are indeed spread to all 
nodes, only a few nodes maintain dormant death certs that are 
never thrown away
Distributed Systems 61

RESERVED MATERIALS
Distributed Systems

Stream -Oriented Communication (1)
Communication as discussed so far has concentrated 
on exchanging more -or-less independent and 
complete units of information
There are forms of comm. in which timing plays a 
crucial role, e.g., an audio stream built up as a 
sequence of 16 -bit samples
Assume that the audio stream represents CD quality, 
meaning that the original sound wave has been sampled at 
a frequency of 44,100 Hz
To reproduce the original sound, it is essential that the 
samples in the audio stream are played out in the order 
they appear in the stream, but also at intervals of exactly 
1 / 44,100 second
Distributed Systems

Stream -Oriented Communication (2)
Support for the exchange of time -dependent info is 
often formulated as support for continuous media
In continuous (representation) media, the temporal 
relationships between different data items are 
fundamental to correctly interpreting what the data 
actually mean , e.g., an audio or video stream
In discrete (representation) media, the temporal 
relationships between data items are not
fundamental to correctly interpreting the data, e.g., 
text, still images, object code or executable files
Distributed Systems

Stream -Oriented Communication (3)
To capture the exchange of time -dependent info, 
DSes generally provide support for data streams
A data stream is a sequence of data units
It can be applied to discrete as well as continuous media
UNIX pipes or TCP/IP connections are typical examples of 
(byte -oriented) discrete data streams
Playing an audio file typically requires setting up a 
continuous data stream between the file and the audio 
device
To capture timing aspects, a distinction is often made 
between different transmission modes: 
asynchronous , synchronous , and isochronous
Distributed Systems

Stream -Oriented Communication (4)
Asynchronous transmission mode
The data items in a stream are transmitted one after the 
other, but there are no further timing constraints on when 
transmission of items should take place
This is typically the case for discrete data streams
Synchronous transmission mode
There is a maximum end -to-end delay defined for each 
unit in a data stream
It may be important that the end -to-end propagation time 
through the network is guaranteed to be lower that the 
time interval between taking samples, but it cannot do any 
harm if samples are propagated faster than necessary
E.g., a sensor sending sample temperature at a certain rate
Distributed Systems

Stream -Oriented Communication (5)
Isochronous transmission mode
It is necessary that data units are transferred on time;  this 
means that data transfer is subject to a maximum and 
minimum end -to-end delay, also referred to as bounded 
(delay) jitter
It plays a crucial role in representing audio and video
Streams can be simple or complex
A simple stream consists of only a single sequence of data
A complex stream consists of several related simple 
streams, called substreams ;  the relation between the 
substreams is often also time dependent
Distributed Systems

Stream -Oriented Communication (6)
From a DS perspective, we can distinguish several 
elements needed for supporting streams
For simplicity, we concentrate on streaming stored data, as 
opposed to streaming live data
We can sketch a general client -server architecture
Distributed Systems


Stream -Oriented Communication (7)
QoS ro erties fro  an a  lication’s  ers ective:
The required bit rate at which data should be transported
The max delay until a session has been set up (i.e., when 
an application can start sending data) 
The max end -to-end delay (i.e., how long it will take until a 
data unit makes it to a recipient)
The max delay variance, or jitter
The max round -trip delay
When dealing with stream -oriented comm. that is 
based on the Internet protocol stack, the basis of 
comm. is formed by an extremely simple, best -effort 
datagram service (i.e., IP) 
Distributed Systems

Stream -Oriented Communication (8)
Given that the underlying system offers only a best -
effort delivery service, a DS can try to conceal as 
much as possible of the lack of QoS
The Internet provides a means for differentiated services;  
a sending host can essentially mark outgoing packets as 
belonging to one of several classes, including an expedited 
forwarding class and an assured forwarding class (by which 
traffic is divided into four subclasses along with three ways 
to drop packets if the network gets congested)
DS may use buffers to 
reduce jitter
Distributed Systems


Stream -Oriented Communication (9)
Given that … (cont’d)
Applying forward error correction (FEC) techniques to 
compensate for the loss in QoS
Since a single packet may contain multiple audio and video 
frames, when it is lost, the receiver may actually perceive a 
large gap when playing out frames;  this can be somewhat 
circumvented by interleaving frames, but this approach 
requires a large receive buffer and thus imposes a higher 
start delay for the receiving application
Distributed Systems


Stream -Oriented Communication (10)
Stream synchronization
Synchronization of streams deals with maintaining 
temporal relations between streams
Sync. between a discrete data stream & a continuous data stream, 
e.g., a slide show enhanced with audio
Sync. between continuous data streams, e.g., a video stream 
synchronized with the audio (lip synchronization), a stereo audio 
stream consisting two substreams
Two issues in stream synchronization:
The basic mechanisms for synchronizing two streams
The distribution of those mechanisms in a networked environment
Sync. mechanisms can be viewed at several different levels 
of abstraction
Distributed Systems

Stream -Oriented Communication (11)
Strea  synchronization (cont’d)
At the lowest level, sync. is done explicitly by operating on 
the data units of simple streams
There is a process that simply executes read and write operations 
on several simple streams, ensuring that those operations adhere 
to specific timing and sync. constraints
Consider a movie presented as 
2 input streams (video & audio)
The video stream contains 
uncompressed low -quality 
images of 320 240 pixels, each 
encoded by a single byte, 
leading to video data units of 
76,800 bytes each;  the images 
are to be displayed at 30 Hz, or 
one image every 33 ms
Distributed Systems


Stream -Oriented Communication (12)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
Consider a  ovie … (cont’d)
The 44.1 kHz, 16 -bit, stereo audio stream contains samples grouped 
into units of 5,880 bytes, each corresponding to 33 ms of audio
If the input process can handle 2.5 Mbps, we can achieve lip sync. by 
simply alternating between reading an image and reading a block of 
audio samples every 33 ms;  the drawback of this approach is that the 
application is made completely responsible for implementing sync. 
while it has only low -level facilities available
A better approach is to offer an interface that allows the 
application to more easily control streams and devices
An application developer can write a simple monitor program 
consisting of two handlers, one for each stream, that jointly check if 
the video and audio streams are sufficiently synchronized, and if 
needed, adjust the rate at which video or audio units are presented
Distributed Systems

Stream -Oriented Communication (13)
Strea  synchronization (cont’d)
At the lowest level … (cont’d)
The last example is typical for multimedia middleware systems
The middleware offers a collection of interfaces for controlling 
audio and video streams, including interfaces for controlling 
devices, e.g., monitors, cameras, microphones, etc.
Each device and stream has 
its own high -level interfaces, 
including interfaces for 
notifying an application 
when some event occurred;  
the latter interfaces are 
subsequently used to write 
handlers for synchronizing 
streams
Distributed Systems


Stream -Oriented Communication (14)
Strea  synchronization (cont’d)
The distribution of synchronization mechanisms
The receiving side of a complex stream needs to know exactly 
what to do;  it must have a complete synchronization specification
locally available
Common practice is to provide this info implicitly by multiplexing the 
different streams into a single stream containing all data units, 
including those for sync.
For an example: the MPEG -2 standard allows an unlimited number of 
continuous and discrete streams to be merged into a single stream
Another issue is whether sync. should take place at the sending or 
receiving side
If the sender handles sync., it may merge streams into a single 
stream with a different type of data units, e.g., a stereo audio stream
The receiver merely has to read in a data unit, and split it into a left 
and right sample;  delays for both channels are now identical
Distributed Systems

"""