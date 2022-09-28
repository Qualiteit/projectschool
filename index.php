<?
include 'FaceTrackingTello.py';
?>
<html>
    <head>
        <title>Drones</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet"><link rel="stylesheet" href="./style.css">
    </head>
<body>
    <div class="display-drone">
        <div class="drone-cam">
            <p>hi</p>
        </div>
        <div class="drone-actions">
            <p>Drone battery:</p>
            <? echo shell_exec("python battery.py"); ?>
        </div>
    </div>
</body>
</html>
