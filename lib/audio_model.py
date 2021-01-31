class AudioModel():
    settings = {
        'version': 1,
        'RATE': 44100,
        'CHANNELS': 2,
        'RECORD_SECONDS': 0.03,
        'SLIDING_WINDOW_AMOUNT': 2,
        'feature_engineering': None
    }
    
    classes_: []
    classifier: None
    
    def __init__(self, settings, classifier):
        self.settings['version'] = settings['version']
        self.settings['RATE'] = settings['RATE']
        self.settings['CHANNELS'] = settings['CHANNELS']
        self.settings['RECORD_SECONDS'] = settings['RECORD_SECONDS']
        self.settings['SLIDING_WINDOW_AMOUNT'] = settings['SLIDING_WINDOW_AMOUNT']
        self.settings['feature_engineering'] = settings['feature_engineering']
        
        self.classifier = classifier
        self.classes_ = classifier.classes_
        if ( self.settings['version'] == 0 ):
            print( "!----Upgrade note-----!" )
            print( "Parrot has added the AudioModel class to encapsulate models." )
            print( "This class aims to provide better backwards compatibility between minor versions." )
            print( "If you are still using the old method, it is encouraged to update using the [C] menu in the settings" )
            print( "-----------------------" )

    def predict_proba(self, data):
        return self.classifier.predict_proba(data)

    def get_setting(self, setting_key, default_value):
        if( setting_key in self.settings ):
            return self.settings[setting_key]
        else:
            return default_value
    
    def get_classifier(self):
        return self.classifier