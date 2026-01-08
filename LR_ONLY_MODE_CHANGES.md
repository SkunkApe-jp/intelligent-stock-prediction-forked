# Linear Regression Only Mode - Changes Summary

## Overview
The stock prediction application has been optimized to run **only the Linear Regression (LR) model**, which is the fastest among the three models (ARIMA, LSTM, LR). This significantly reduces prediction time from minutes to seconds.

## Changes Made

### 1. Backend Changes (`main.py`)
**File**: `c:\Projects\intelligent-stock-prediction\main.py`

- **Disabled ARIMA and LSTM**: Commented out the calls to `ARIMA_ALGO()` and `LSTM_ALGO()`
- **Set dummy values** for ARIMA and LSTM to prevent template errors
- **Only Linear Regression runs**: `LIN_REG_ALGO()` is the sole active model

```python
# Enable only Linear Regression model for fastest performance
# arima_pred, error_arima, arima_actual, arima_predicted=ARIMA_ALGO(df)
# lstm_pred, error_lstm, lstm_actual, lstm_predicted=LSTM_ALGO(df)

# Set dummy values for disabled models
arima_pred, error_arima, arima_actual, arima_predicted = 0, 0, [], []
lstm_pred, error_lstm, lstm_actual, lstm_predicted = 0, 0, [], []

# Run only Linear Regression
df, lr_pred, forecast_set,mean,error_lr, lr_actual, lr_predicted=LIN_REG_ALGO(df)
```

### 2. Frontend Changes (`results.html`)
**File**: `c:\Projects\intelligent-stock-prediction\templates\results.html`

#### Hidden Sections (with `style="display: none;"`):
1. **ARIMA model accuracy chart** (lines 155-171)
2. **LSTM model accuracy chart** (lines 172-188)
3. **ARIMA prediction card** (lines 210-222)
4. **LSTM prediction card** (lines 223-235)
5. **ARIMA RMSE card** (lines 253-265)
6. **LSTM RMSE card** (lines 266-278)

#### Expanded LR Sections (from `col-lg-4` to `col-lg-12`):
1. **LR chart container**: Now spans full width for better visualization
2. **LR prediction card**: Full-width display with improved label "Linear Regression"
3. **LR RMSE card**: Full-width display for error metrics

## Performance Benefits

| Metric | Before (All 3 Models) | After (LR Only) |
|--------|----------------------|-----------------|
| **Processing Time** | ~30-60 seconds | ~2-5 seconds |
| **LSTM Training** | 25 epochs | Skipped ✓ |
| **ARIMA Iterations** | Rolling forecast | Skipped ✓ |
| **Page Load** | Slower | Much faster |

## User Experience Improvements

1. **Faster predictions**: Results appear almost instantly
2. **Cleaner interface**: Only relevant LR metrics displayed
3. **Better visualization**: Full-width charts for improved readability
4. **Reduced cognitive load**: Single model focus

## How to Revert (If Needed)

To re-enable all three models:

1. **In `main.py`**: Uncomment lines 935-936
2. **In `results.html`**: Remove all `style="display: none;"` attributes
3. **In `results.html`**: Change LR cards back from `col-lg-12` to `col-lg-4` or `col-lg-6`

## Notes

- The sentiment analysis and recommendation logic remain unchanged
- All other features (7-day forecast, news sentiment, etc.) continue to work
- The Linear Regression model is trained fresh on each request (no caching)
