<?php
//載入 db.php 檔案，讓我們可以透過它連接資料庫
require_once 'php/db.php';
require_once 'php/functions.php';
$datas = get_publish_article();
?>
<!DOCTYPE html>
<html lang="zh-TW">
  <head>
    <title>tripresso</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <!-- 給行動裝置或平板顯示用，根據裝置寬度而定，初始放大比例 1 -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 載入 bootstrap 的 css 方便我們快速設計網站-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="css/style.css"/>
    <link rel="shortcut icon" href="images/favicon.ico">
  </head>

  <body>
    <!-- 頁首 -->

    <div class="jumbotron">
      <div class="container">
        <!-- 建立第一個 row 空間，裡面準備放格線系統 -->
        <div class="row">
          <!-- 在 xs 尺寸，佔12格，可參考 http://getbootstrap.com/css/#grid 說明-->
          <div class="col-xs-12">
            <!--網站標題-->
            <h1 class="text-center">所有文章</h1>

            <!-- 選單 -->
            <ul class="nav nav-pills">
              <li role="presentation" class="active"><a href="index.php">首頁</a></li>
              <li role="presentation"><a href="article_list.php">所有文章</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- 網站內容 -->
    <div class="content">
      <div class="container">
        <!-- 建立第一個 row 空間，裡面準備放格線系統 -->
        <div class="row">
          <!-- 在 xs 尺寸，佔12格，可參考 http://getbootstrap.com/css/#grid 說明-->
          <div class="col-xs-12">
          	<?php if(!empty($datas)):?>
          	<?php foreach($datas as $article):?>	
          	<div class="panel panel-primary">
						        <div class="panel-heading">
						        	<?php echo $article['title'];?>
						        </div>
						        <div class="panel-body">		
						        	<p>
						        		出發日期: <span class="label label-info"><?php echo $article['date'];?></span>
						        		旅遊天數: <span class="label label-danger"><?php echo $article['trip_date'];?>天</span>	
						        		價格: <span class="label label-info"><?php echo $article['price'];?></span>
						        		總團位: <span class="label label-danger"><?php echo $article['all_set'];?></span>
			                                                      可售位: <span class="label label-info"><?php echo $article['sale_set'];?></span>	
						        	</p>
						        </div>
						    </div>
						 <?php endforeach; ?>
						 <?php endif; ?>
          </div>
        </div>
      </div>
    </div>

    <!-- 頁底 -->
    <div class="footer">
      <div class="container">
        <!-- 建立第一個 row 空間，裡面準備放格線系統 -->
        <div class="row">
          <!-- 在 xs 尺寸，佔12格，可參考 http://getbootstrap.com/css/#grid 說明-->
          <div class="col-xs-12">
            <p class="text-center">
              &copy; <?php echo date("Y")?>
              Jason.
            </p>
          </div>
        </div>
      </div>

    </div>

    <?php
    //結束mysql連線
    //mysql_close();
    ?>
  </body>
</html>