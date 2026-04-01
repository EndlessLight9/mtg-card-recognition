import cv2

#Usamos detector ORB
#Ele procura por pontos de interesse da imagem, como bordas
#Para cada ponto de interesse, gera um descritor, que descreve matemáticamente os pixeis arredor desse ponto
#compara os descritores de uma imagem com os descritores de outra imagem, para encontrar correspondências entre os pontos de interesse
orb = cv2.ORB_create(nfeatures=1000)

#iniciamos o comparador

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


def extract_features(image_path):
    """
    Reads an image, padronizes its size and extracts ORB features.
    """

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print(f"Error reading image: {image_path}")
        return None
    
    # redimensiona imagem para um tamanho padrão
    image_resized = cv2.resize(image, (300,418))

    # ORB detecta os pontos e calcula a matriz de descritores

    keypoints, descriptors = orb.detectAndCompute(image_resized, None)

    return descriptors

def compare_cards(descriptors_test, descriptors_db):
    """
    Compares the descriptors of a test card with the descriptors of a database card and returns the number of good matches.
    """
    if descriptors_test is None or descriptors_db is None:
        return 0
    
    matches = bf.match(descriptors_test, descriptors_db)
    good_matches = [m for m in matches if m.distance < 50] 
    return len(good_matches)

if __name__ == "__main__":
    print("Engine module loaded. Ready to extract features and compare cards.")
