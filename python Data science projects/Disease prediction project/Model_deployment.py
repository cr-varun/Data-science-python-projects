import pickle
import flask
def load_pickle(filename):
    with open('data/'+filename,'rb') as f:
        return pickle.load(f)

drop_col_l = load_pickle('drop_col.pkl')
encoded_symptoms = load_pickle('encodedSymp.pkl')
StandardScaler = load_pickle('StandardScaler.pkl')
model_pickle = load_pickle('model.pkl')
nul_replace = load_pickle('nul_replace.pkl')


def do_prediction(sample):
    if 'Disease' in sample:
        sample.drop('Disease',axis=1,inplace = True)
    sample.fillna(nul_replace,inplace = True)    
    sample.drop(drop_col_l,axis=1,inplace = True)
    print(encoded_symptoms)
  
    for col in sample.columns:
        print(col , " ",sample[col])
        #sample[col] = sample[col].str.strip()
        sample[col] = sample[col].map(encoded_symptoms)
    sample = StandardScaler.transform(sample)
    return model_pickle.predict(sample)






