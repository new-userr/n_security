from PIL import Image
import stepic

#ENCRYPTION

original_img=Image.open('img1.jpg')

encoded_img=stepic.encode(original_img,b'hello this is ns practical')
                        
encoded_img.save('img2.png')
                    
encoded_img=Image.open('img2.png')

encoded_img.show()

#DECRYPTION

decoded_img=stepic.decode(encoded_img)
print("the decoded message is >>", decoded_img)