<?php

$url="https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775";
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, $url);
$data = curl_exec($ch);
curl_close($ch);

$xml = simplexml_load_string($data);
$today = $xml->Cube->Cube['time'];
$usdRate = $xml->Cube->Cube->Cube['rate'];
$currencies = $xml->Cube->Cube->Cube;

$csvArray = array();
array_push($csvArray, array("Currency Code", "Rate"));

for ($i = 0; $i < count($currencies); $i++) {
    $currentCurrency = (string)$currencies[$i]['currency'];
    $currentRate = $currencies[$i]['rate'];
    $usdConvertedRate = (double)$currentRate / (double)$usdRate;
    $pushArray = array($currentCurrency, $usdConvertedRate);
    array_push($csvArray, $pushArray);
}

$file = fopen("usd_currency_rates_$today.csv", "w");

foreach ($csvArray as $fields) {
    fputcsv($file, $fields);
}

fclose($file);

?>