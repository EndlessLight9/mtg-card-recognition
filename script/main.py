import os
import glob

from engine import extract_features, compare_cards

def identify_card(test_image_path, database_dir):
    """
    Mainn function that receives a photo and sweeps through the database to find the best match.
    """

    test_image_name = os.path.basename(test_image_path)
    print(f"Identifying card: {test_image_name}")

    # extract features from image received as input

    descriptors_test = extract_features(test_image_path)

    if descriptors_test is None:
        print(f"Could not extract features from the test image: {test_image_name}")
        return None
    
    #variaveis auxiliares só para guardar o ganhador
    top_score = 0
    identify_card = "TBD"

    # sweep through the database

    db_images = glob.glob(os.path.join(database_dir, "*.jpg"))
    print(f"Comparing with {len(db_images)} card found in the database...")

    #loop para busca por similiridade

    for db_image_path in db_images:
        #extract features from the database image
        descriptors_db = extract_features(db_image_path)

        #engine compara os dados e diz quantos pontos bateram

        current_score = compare_cards(descriptors_test, descriptors_db)

        if current_score > top_score:
            top_score = current_score
            identify_card = os.path.basename(db_image_path).replace(".jpg", "")

    print(f"Identified card: {identify_card} with score: {top_score}")


if __name__ == "__main__":
    #definimos pastas
    test_image_path = "/home/endless_light/mtg-card-recognition/images"
    database_dir = "/home/endless_light/mtg-card-recognition/scryfall_data"

    all_test_images = glob.glob(os.path.join(test_image_path, "*.jpg")) 

    #se encontrou alguma imagem, roda o sistema para a primeira que achar

    if len(all_test_images) > 0:
        for image in all_test_images:
            identify_card(image, database_dir)
    else:
        print("No test images found in the specified directory.")
