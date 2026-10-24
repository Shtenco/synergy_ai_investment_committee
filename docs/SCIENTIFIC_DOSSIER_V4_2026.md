# INVESTMENT COMMITTEE / MULTI-AGENT THESIS

## Научная задача и собственный исследовательский вклад

Momentum / risk / liquidity / bounded advice. Three implemented specialist agents generate scored votes using market momentum, volatility and liquidity. deliberate averages votes, applies hard volatility veto and returns BUY/SELL/NO_TRADE. Its capital_guardian field marks advisory status; no live order is placed by this core.

## Фактический вычислительный механизм

Score = mean(vote scores); if volatility >= 0.20 the action is NO_TRADE, otherwise BUY for score>0.2, SELL for score< -0.2, else NO_TRADE. Agent scores are heuristic and not calibrated probabilities.

## Почему этот компонент важен для единой федерации

Это отдельный специализированный компонент — источник ограниченного, объяснимого исследования или решения. Его выводы можно передавать по типизированному контракту, не делая саму модель хозяином клиентских средств или бухгалтерского результата.

## Программа воспроизводимого эксперимента

Study agent disagreement, heterogeneous forecasts, confidence calibration, stress regimes and human committee comparison. Preserve each vote with a quote timestamp and run ablations to measure whether deliberation outperforms each component.

## Экспериментальный протокол и измеримые результаты

Зафиксировать исходный commit, датированные входы и их SHA-256, строгий baseline, независимую валидационную и тестовую выборки, граничные случаи, стоимость вычисления и неблагоприятные сценарии. Сравнивать на одном времени и идентичном объёме ресурсов. Публиковать не только mean score, но и распределение ошибок, устойчивость, отказные сценарии и экономические издержки. Наличие исполняемых тестов и enterprise API не доказывает реальную финансовую эффективность или production deployment.

## Подтверждающие исходники

- [`src/synergy_ai_committee/core.py`](../src/synergy_ai_committee/core.py)
- [`src/synergy_ai_committee/synergy_contracts.py`](../src/synergy_ai_committee/synergy_contracts.py)
- [`tests/`](../tests/)

## Критерий следующей версии

Перейти от предметного реализованного ядра к эксперименту с отдельным воспроизводимым manifest, автоматической CI-проверкой и фактическими доказательствами из конечной интеграции. Прежняя корневая документация сохранена полностью.
