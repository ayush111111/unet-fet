Fetal Head segmentation using U-Net

Built an HC18 fetal-head ultrasound segmentation and circumference-estimation pipeline; found that a frozen ImageNet-pretrained EfficientNetB4 encoder limited adaptation of skip features to ultrasound speckle and weak boundaries, so moved to trainable custom U-Net variants, diagnosed low sensitivity despite Dice plateaus, and used Bayesian tuning to achieve 97.87% Dice and 1.95 ± 1.86 mm mean absolute difference on challenge evaluation.


https://ayush111111.github.io/quartz/notes/2023-04-26-Automated-Head-Circumference-Measurement
