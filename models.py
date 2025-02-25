from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HeartDiseasePrediction(db.Model):
    """
    A class used to represent a Heart Disease Prediction entry.

    Attributes
    ----------
    id : int
        The unique identifier for the prediction entry
    age : int
        Age of the patient
    sex : int
        Sex of the patient (1 = male; 0 = female)
    cp : int
        Chest pain type (0-3)
    trestbps : int
        Resting blood pressure (in mm Hg on admission to the hospital)
    chol : int
        Serum cholesterol in mg/dl
    fbs : int
        Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    restecg : int
        Resting electrocardiographic results (0-2)
    thalach : int
        Maximum heart rate achieved
    exang : int
        Exercise induced angina (1 = yes; 0 = no)
    oldpeak : float
        ST depression induced by exercise relative to rest
    slope : int
        The slope of the peak exercise ST segment (0-2)
    ca : int
        Number of major vessels (0-3) colored by fluoroscopy
    thal : int
        Thalassemia (1-3)
    target : int
        Diagnosis of heart disease (1 = disease; 0 = no disease)
    """
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    trestbps = db.Column(db.Integer, nullable=False)
    chol = db.Column(db.Integer, nullable=False)
    fbs = db.Column(db.Integer, nullable=False)
    restecg = db.Column(db.Integer, nullable=False)
    thalach = db.Column(db.Integer, nullable=False)
    exang = db.Column(db.Integer, nullable=False)
    oldpeak = db.Column(db.Float, nullable=False)
    slope = db.Column(db.Integer, nullable=False)
    ca = db.Column(db.Integer, nullable=False)
    thal = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    
    def to_dict(self) -> dict:
        """
        Convert the Heart Disease Prediction instance to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the Heart Disease Prediction instance.
        """
        return {
            'id': self.id,
            'age': self.age,
            'sex': self.sex,
            'cp': self.cp,
            'trestbps': self.trestbps,
            'chol': self.chol,
            'fbs': self.fbs,
            'restecg': self.restecg,
            'thalach': self.thalach,
            'exang': self.exang,
            'oldpeak': self.oldpeak,
            'slope': self.slope,
            'ca': self.ca,
            'thal': self.thal,
            'target': self.target
        }
