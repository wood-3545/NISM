# NISM Dataset Structure Description

### 1. EMG: Raw Electromyography Data

```
- EMG
   |-- user1
   |-- ...
   |-- user20
```

Each `user` folder contains 20 files named:

```
aligned_emg_1.csv ~ aligned_emg_20.csv
```

The numbers `1–20` correspond to the 20 different hand gestures or grasp actions.

### 2. IMU: Includes Accelerometer and Quaternion Data

```
- IMU
   |-- user1
        |-- WT1
        |-- WT2
        ...
        |-- WT6
   |-- ...
   |-- user20
        |-- WT1
        |-- WT2
        ...
        |-- WT6
```

Each `WT{num2}` subfolder contains files named:

```
{num1}_WT{num2}.csv
```

Where:
- `num1` corresponds to the 20 gestures (`1–20`),
- `num2` indicates the IMU sensor index (`1–6`).

### 3. Keypoint: Hand Keypoints Extracted from Video

Keypoints were extracted from RGB videos and then normalized using scaling, rotation, and translation for stable alignment.

```
- keypoint
   |-- user1
   |-- ...
   |-- user20
```

Each `user` folder contains 20 files named:

```
1_keypoints_smoothed.csv ~ 20_keypoints_smoothed.csv
```

Each file represents one of the 20 hand gestures.

### 4. Pressure: Finger Pressure Data

```
- Pressure
   |-- user1
        |-- 1
        |-- 2
        ...
        |-- 20
   |-- ...
   |-- user20
        |-- 1
        |-- 2
        ...
        |-- 20
```

Each `user` folder contains 20 subfolders (named `1–20`, corresponding to the gestures).  
Each of these contains five files named:

```
aligned_pressure_f1_newton.csv ~ aligned_pressure_f5_newton.csv
```

These represent pressure data for the five fingers: thumb to little finger.
