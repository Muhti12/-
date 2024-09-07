from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
def model_keras(modelyolu, gorselyolu, labelyolu ):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(modelyolu, compile=False)

    # Load the labels
    class_names = open(labelyolu, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(gorselyolu).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    if index == 0:
       return (f" Görsleinizi sınıflandırdık ve sonuç olarak {class_name} sınıfına yerleştirdik. Aynı zamanda güvenilirlik skorunu {confidence_score} olarak bulduk.Bu bağlamda size birkaç önerimiz olacak: \n Bu kömür ve fosil yakıtlardan biridir. Küresel ısınmaya zararlıdır ve küresel ısınmanın temel nedenlerindendir")
    if index == 1:
        return (f" Görsleinizi sınıflandırdık ve sonuç olarak {class_name} sınıfına yerleştirdik. Aynı zamanda güvenilirlik skorunu {confidence_score} olarak bulduk.Bu bağlamda size birkaç önerimiz olacak: \nBu doğal gaz ve fosil yakıtlardan biridir. Küresel ısınmaya Kömür ve petrolden daha az zararlıdır")
    if index == 2:
       return (f" Görsleinizi sınıflandırdık ve sonuç olarak {class_name} sınıfına yerleştirdik. Aynı zamanda güvenilirlik skorunu {confidence_score} olarak bulduk.Bu bağlamda size birkaç önerimiz olacak: \nBu petrol ve fosil yakıtlardandır. doğal gazdan fazla kömürden az zararlıdır")
    else:
        return ("Bu fotoğraf küresel ısınmaya zararsız")

