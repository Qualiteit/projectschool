<?
include 'FaceTrackingTello.py';
// Including facetracking
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
        <canvas id="video-canvas"></canvas>
            <script type="text/javascript" src="jsmpeg.min.js"></script>
            <script type="text/javascript">
                var canvas = document.getElementById('video-canvas');
                var url = 'ws://'+document.location.hostname+':3001/stream';
                var player = new JSMpeg.Player(url, {canvas: canvas});
            </script>
        </div>
        <div class="drone-actions">
            <p>Drone battery:</p> 
            <? echo shell_exec("python battery.py"); ?>
        <button class="connect-button button-general">Connect</button>
        <button class="takeoff-button button-general">Takeoff</button>
        <button class="land-button button-general">Land</button>
        <button class="handcontrol-button button-general">Hand controls</button>
        <button class="facetracking-button button-general">Face tracking</button>
        </div>
    </div>
</body>
</html>
