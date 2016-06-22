#Web Apps 期末project

##簡介
一共有兩個demo，都是用Django實作的restful api
並且提供簡單的client範例

##Demo 1
每周會從題庫找四個題目，然後利用Django的admin，把題單存進DB  
只要利用 http://your-domain/ph/<week> 就可以取得<week>該周的題單，格式json  
然後client就可以根據題單，自動找對應的檔案壓縮上傳FTP

##Demo 2
利用Django + rest framework快速建置一個縮網址服務，會根據拿到的long_url隨機建立對應的short_url
然後client可以利用AJAX呼叫restful api取得縮網址<token>，但是要注意javascript的cross domain的問題
然後用瀏覽器呼叫 http://your-domain/<token> 就可以自動轉址到對應的long_url了
而且DB裡面有click conter，可以知道這個縮網址被使用了幾次
