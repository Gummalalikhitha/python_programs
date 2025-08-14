 # 1.kmeans
# 2.data parameters (number of clusters -k)
# 3.model 
# 4.fit 
# 5.cluster analyze

#cluster -k means --we have to findk number of centroids
'''
from sklearn.cluster import KMeans 
import numpy as np
import matplotlib.pyplot as plt 
x=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
kmeans=KMeans(n_clusters=2,random_state=42)
kmeans.fit(x)
plt.scatter(x[:,0],x[:,1],c=kmeans.labels_,cmap="rainbow")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c="black",marker="x")
plt.show()

'''
#cluster with 3D
'''
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score
import pandas as pd 

rng=np.random.default_rng()
n_per_cluster=[450,400,350,300]
means=np.array([[0,0,0],[6.5,6.5,5.5],[-6,6.5,6.5]])
covs=[np.array([[1.2,0.2,0.0],[0.2,1.0,0.1],[0.0,0.1,0.8]]),
      np.array([[1.5,0.3,0.1],[0.3,1.8,0.2],[0.1,0.2,1.0]]),
      np.array([[0.9,-0.2,0.0],[-0.2,1.3,0.1],[0.0,0.1,1.1]]),
      np.array([[1.1,0.0,-0.1],[0.0,1.0,0.0],[-0.1,0.0,1.4]]),
      ]
clusters=[rng.multivariate_normal(m,c,size=n) for n,m,c in zip(n_per_cluster,means,covs)]
x=np.vstack(clusters)
x=x[rng.permutation(len(x))]
k=4
kmeans=KMeans(n_clusters=k,n_init=10,random_state=42)
labels=kmeans.fit_predict(x)
sil=silhouette_score(x,labels)
print(f"Sillhoutte score:{sil:.3f}")
sizes=pd.Series(labels).value_counts().sort_index()
summary_df=pd.DataFrame({'cluster_id':sizes.index,'n_points':sizes.values})
summary_df['fraction']=summary_df['n_points']/len(x)
summary_df['centroid_x']=np.round(kmeans.cluster_centers_[:,0],3)
summary_df['centroid_y']=np.round(kmeans.cluster_centers_[:,1],3)
summary_df['centroid_z']=np.round(kmeans.cluster_centers_[:,2],3)

print("\n Cluster Summary:",summary_df)

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection="3d")
ax.scatter(x[:,0],x[:,1],x[:,2],c=labels,s=10)
ax.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,2],marker='x',s=200,edgecolors='black')
plt.tight_layout()
plt.show()
'''

#Doreamon 3D
'''
import numpy as np
import matplotlib.pyplot as plt

def sphere(center, radius, n_points=50):
    phi = np.linspace(0, np.pi, n_points)
    theta = np.linspace(0, 2 * np.pi, n_points)
    phi, theta = np.meshgrid(phi, theta)
    x = center[0] + radius * np.sin(phi) * np.cos(theta)
    y = center[1] + radius * np.sin(phi) * np.sin(theta)
    z = center[2] + radius * np.cos(phi)
    return x.flatten(), y.flatten(), z.flatten()

fig = plt.figure(figsize=(8,10))
ax = fig.add_subplot(111, projection='3d')

# Head (blue sphere)
x_head, y_head, z_head = sphere(center=[0,0,0], radius=1)
ax.scatter(x_head, y_head, z_head, color='blue', alpha=0.6, s=8)

# Face (white sphere, smaller, overlapping lower front)
x_face, y_face, z_face = sphere(center=[0,0,0.3], radius=0.85)
ax.scatter(x_face, y_face, z_face, color='white', alpha=0.9, s=8)

# Eyes (white small spheres)
x_eye1, y_eye1, z_eye1 = sphere(center=[-0.3,0.8,0.6], radius=0.2)
ax.scatter(x_eye1, y_eye1, z_eye1, color='white', s=10)

x_eye2, y_eye2, z_eye2 = sphere(center=[0.3,0.8,0.6], radius=0.2)
ax.scatter(x_eye2, y_eye2, z_eye2, color='white', s=10)

# Pupils (black small spheres)
x_pupil1, y_pupil1, z_pupil1 = sphere(center=[-0.3,0.95,0.6], radius=0.07)
ax.scatter(x_pupil1, y_pupil1, z_pupil1, color='black', s=20)

x_pupil2, y_pupil2, z_pupil2 = sphere(center=[0.3,0.95,0.6], radius=0.07)
ax.scatter(x_pupil2, y_pupil2, z_pupil2, color='black', s=20)

# Nose (red small sphere)
x_nose, y_nose, z_nose = sphere(center=[0,1.05,0.45], radius=0.15)
ax.scatter(x_nose, y_nose, z_nose, color='red', s=30)

# Body (blue bigger sphere below head)
x_body, y_body, z_body = sphere(center=[0,0,-1.5], radius=1.5)
ax.scatter(x_body, y_body, z_body, color='blue', alpha=0.6, s=8)

# Belly (white sphere on body)
x_belly, y_belly, z_belly = sphere(center=[0,0,-1.2], radius=1.1)
ax.scatter(x_belly, y_belly, z_belly, color='white', alpha=0.9, s=8)

ax.set_box_aspect([1,1,1.5])
ax.set_xlim(-2,2)
ax.set_ylim(-1,2)
ax.set_zlim(-3,1)

ax.axis('off')
plt.title("Simple 3D Doraemon-like Figure (Cartoonish)")
plt.show()
'''
#Main Libraries of NLP
'''
NLTK
SpaCy 
Gensim 
Scikit-learn
CoreNLP 
'''
#pos_ner_tok 
# pip install spacy
# python -m spacy download en_core_web_sm
'''
import spacy 
nlp=spacy.load("en_core_web_sm")
text="Apple is launching a new iphone in New York on september 10,2025 "
doc=nlp(text)
print("Tokens") 
for token in doc:
    print(token.text,end=" | ")
print('\n\n parts-of-spech Tags')
for token in doc:
    print(f"{token.text}:{token.pos_}(token.tag_)")
print("\n data-> name")
for ent in doc.ents:
    print(f"{ent.text}:{ent.label_}")

'''

#stop words
'''
import spacy 
nlp=spacy.load("en_core_web_sm")
text="I love to study in NRIIT Agiripalli"
doc=nlp(text)

filtered_tokens=[token.text for token in doc if not token.is_stop]
print([token.text for token in doc])
print(filtered_tokens)

'''
#Lemmitization
#v2 or v3 or v4 to v1 verb
'''
import spacy 
nlp=spacy.load("en_core_web_sm")
text="I was running and studying while othersplayed."
doc=nlp(text)
lt=[token.lemma_ for token in doc]
print([token.text for token in doc])
print(lt)
'''
#Sentiment Analysis
#rcParams is used to access the emojis
# pip install textblob
from textblob import TextBlob 
from matplotlib import rcParams
rcParams['font.family']="Segoe UI Emoji"
texts="Vijay is happy"
def sentiment_face(polarity):
    if polarity>0.1:
        return "😀"
    elif polarity<-0.1:
        return "😢"
    else:
        return "😐"
blob=TextBlob(texts)
face=sentiment_face(blob.sentiment.polarity)
print(face)
