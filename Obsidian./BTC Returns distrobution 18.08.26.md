DATA spec.
Timeframes 1m,5m,15m,30m,1h,4h,1d. - resample from native 1m 
Структура данних CSV:
Open time, Open, High, Low, Close, Volume, Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore.
From 2017-08 to 2026-06.
Close to Close Log returns 

Якщо видалити нулі в дохідностях - то після resample в інший часовий маштаб буде недостаньо хвилин. Врахуємо що нулі це природа 1хв дохідностей. Єдине що ті періоди це час пропускаєтся,будемо щось думати.

