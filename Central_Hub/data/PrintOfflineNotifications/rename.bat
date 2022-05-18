echo off:


ren "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\instiintari_pdf\*.pdf" "0.pdf"
ren "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\raport_vanzari\*.xls" "0.xls"
copy "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\*.xls" "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\1.xls"
move "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\1.xls" "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\tabel_no_mail\"
del "C:\Users\andrei.astelian\Desktop\Central_Hub\data\PrintOfflineNotifications\*.xls"

popd

