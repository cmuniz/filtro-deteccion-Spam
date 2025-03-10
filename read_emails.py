from email_parser import EmailParser

def leer_correos(root_path, num):
    
    labels_path = root_path + r"/full/index"
    with open(labels_path, 'r') as f:
        labels = f.read().splitlines()
        
    # Leemos los correos de disco
    X = []
    y = []
    for l in labels[:num]:
        label, email_path = l.split(' ../')
        y.append(label)
        with open(root_path + "/" + email_path, errors='ignore') as f:
            X.append(f.read())
            
    return X, y



def crear_dataset(indice, num):
    email_parser = EmailParser()
    X, y = leer_correos(indice, num)
    X_proc = []
    for i, email in zip(range(len(X)), X):
        print("\rParsing email: {0}".format(i+1), end='')
        X_proc.append(email_parser.parse(email))
    return X_proc, y

if __name__ == "__main__":
    X, y = leer_correos("email-dataset", 10)
    