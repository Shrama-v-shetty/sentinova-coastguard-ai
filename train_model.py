from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# Load dataset
train_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(
    'dataset/train',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary'
)

# Pretrained model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(128,128,3))
base_model.trainable = False

# Custom model
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(train_data, epochs=3)

# Save model
model.save("crack_model.h5")

print("Model trained and saved!")