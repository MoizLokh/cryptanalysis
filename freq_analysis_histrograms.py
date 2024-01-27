from collections import Counter
import matplotlib.pyplot as plt

#  cipher text provided by  user
cipher_text = "YHZOZJBDACYHQAFDCWZONOZMBOPBRLZQAYHBYACOUQUBLQGZYHQAPQYDCWZONMIGHCIYCVYHZJBNYCHZBOYHZOBRRQYDBNYCQYDZLVGCMMBCHUZBOCHUZBOQDHBLLRZLBYZJHZADHZYHCIFHYQYCWZOBVYZOJBOUDGCMMBQYCGGIOOZUYCHZOYHBYDHZCIFHYYCHBWZJCAUZOZUBYYHQDGCMMBRIYBYYHZYQMZQYBLLDZZMZUtIQYZABYIOBLRIYJHZAYHZOBRRQYBGYIBLLNYCCPBJBYGHCIYCVQYDJBQDYGCBYXCGPZYGCMMBBAULCCPZUBYQYGCMMBBAUYHZAHIOOQZUCAGCMMBBLQGZDYBOYZUYCHZOVZZYGCMMBVCOQYVLBDHZUBGOCDDHZOMQAUYHBYDHZHBUAZWZORZVCOZDZZABOBRRQYJQYHZQYHZOBJBQDYGCBYXCGPZYGCMMBCOBJBYGHYCYBPZCIYCVQYGCMMBBAURIOAQAFJQYHGIOQCDQYNGCMMBDHZOBABGOCDDYHZVQZLUBVYZOQYGCMMBBAUVCOYIABYZLNJBDSIDYQAYQMZYCDZZQYXCXUCJABLBOFZOBRRQYHCLZIAUZOYHZHZUFZ"


for k in range(2,5):
    # Extracting bigrams from  text
    bigrams = [cipher_text[i:i+k] for i in range(len(cipher_text)-1)]

    # Counting  frequency of each bigram
    bigram_counts = Counter(bigrams)

    # Selecting  top 30 most frequent bigrams for  histogram
    most_common_bigrams = bigram_counts.most_common(30)
    bigram_labels, counts = zip(*most_common_bigrams)

    # Creating  histogram
    plt.figure(figsize=(15, 7))
    plt.bar(bigram_labels, counts, color='blue')
    plt.xlabel('Bigrams')
    plt.ylabel('Frequency')
    plt.title('Frequency of Top 30 Bigrams in  Cipher Text')
    plt.xticks(rotation=45)
    plt.show()
