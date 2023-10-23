def fix_activity(string):
        string = str(string).lower().strip()
        if string != string:
            return np.nan
        elif "swimming" in string or "bathing" in string or "floating" in string or "splashing" in string or "jumped into the water" in string or "playing" in string:
            return "swimming"
        elif "diving" in string or "snorkel" in string:
            return "diving"
        elif "fish" in string:
            return "fishing"
        elif "surf" in string or "body boarding" in string or "body-boarding" in string or "boogie boarding" in string or "paddleskiing" in string:
            return "surf"
        elif "standing" in string or "paddling" in string or "paddl" in string:
            return "paddling"
        elif "kayaking" in string or "ship" in string or "sail" in string or "boat" in string or "canoeing" in string or "board" in string or "rowing" in string or "fell" in string:
            return "boating"
        elif "disaster" in string:
            return "sea disaster"
        elif "wading" in string or "walking" in string or "treading water" in string or "feed" in string:
            return "walking"
        else:
            return "others"


def fix_cols(df):
    clean_lst = []
    for c in df.columns:
        c = c.strip().upper()
        clean_lst.append(c)
    df.columns = clean_lst
    return df.columns

def change_col(df,old,new):
    df.rename(columns={old:str.upper(new)},inplace = True)