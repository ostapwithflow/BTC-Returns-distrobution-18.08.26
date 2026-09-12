DATA spec.
Timeframes 1m,5m,15m,30m,1h,4h,1d. - resample from native 1m 

Структура данних CSV:
Open time, Open, High, Low, Close, Volume, Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore.

Close to Close Log returns 
Данні з сайту: https://data.binance.vision

Якщо видалити нулі в дохідностях - то після resample в інший часовий маштаб буде недостаньо хвилин. Врахуємо що нулі це природа 1хв дохідностей. Єдине що ті періоди це час пропускаєтся,будемо щось думати.


Винятки:
2017 від 08-17 починаєтся (не повний рік)
2026 до 07-31 (включно) (не повний рік)

шлях:
1) всі файли olhc перевелятся в єдиний великий файл 
2) Перевіряєтся на збіжність рядків 
3) Timestaps перевідятся в utc
4) Розрахунок log returns в окремий csv файл і фільтрація доходностей які не відповідають таймфрейму.

