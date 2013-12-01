import sciunit
import sciunit.scores

class RatioComparator(sciunit.Comparator):
    """Returns a score indicating the ratio of model to reference means."""  
    def __init__(self,*args,**kwargs):
        super(RatioComparator,self).__init__(*args,**kwargs)
        self.required_model_stats += ('value',)
        self.required_reference_stats += ('mean',)
        
    score_type = sciunit.scores.RatioScore

    def compute(self,**kwargs):
        m_value = self.model_stats['value']
        r_mean = self.reference_stats['mean']
        return (m_value+0.0)/r_mean

class ZComparator(sciunit.Comparator):
    """Returns a score indicating the Z-score of the model value relative to the 
    reference mean and standard deviation."""  
    def __init__(self,*args,**kwargs):
        super(ZComparator,self).__init__(*args,**kwargs)
        self.required_model_stats += ('value',)
        self.required_reference_stats += ('mean','std',)    
        
    score_type = sciunit.scores.ZScore

    def compute(self,**kwargs):
        m_value = self.model_stats['value']
        r_mean = self.reference_stats['mean']
        r_std = self.reference_stats['std']
        return (m_value - r_mean)/r_std

"""Converters for converting from one (raw) score to another kind of (raw) score.
The converter attribute of a Comparator or a Test can be set to one of these."""

def ZScoreToBooleanScore(self,Z,params={'thresh':2}):
    """Converts a ZScore class to a BooleanScore class."""  
    thresh = params['thresh'] # +/- Threshold within which Z must stay to pass.  
    boolean = -thresh <= Z.score <= thresh
    return sciunit.scores.BooleanScore(boolean)
    