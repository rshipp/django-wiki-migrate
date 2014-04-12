# JavaScript functions from Django and Django-wiki.
# -*- coding: iso-8859-15 -*-

URLIFY = ("""
var LATIN_MAP = {
    'Ã': 'A', 'Á': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'AE', 'Ã':
    'C', 'Ã': 'E', 'Ã': 'E', 'Ã': 'E', 'Ã': 'E', 'Ã': 'I', 'Í': 'I', 'Ã': 'I',
    'Ï': 'I', 'Ð': 'D', 'Ã': 'N', 'Ã': 'O', 'Ã': 'O', 'Ã': 'O', 'Ã': 'O', 'Ã':
    'O', 'Ő': 'O', 'Ã': 'O', 'Ã': 'U', 'Ã': 'U', 'Ã': 'U', 'Ã': 'U', 'Ű': 'U',
    'Ý': 'Y', 'Ã': 'TH', 'Ã': 'ss', 'Ã':'a', 'á':'a', 'â': 'a', 'ã': 'a', 'ä':
    'a', 'å': 'a', 'æ': 'ae', 'ç': 'c', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
    'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ð': 'd', 'ñ': 'n', 'ò': 'o', 'ó':
    'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'Å': 'o', 'ø': 'o', 'ù': 'u', 'ú': 'u',
    'û': 'u', 'ü': 'u', 'ű': 'u', 'ý': 'y', 'þ': 'th', 'ÿ': 'y'
}
var LATIN_SYMBOLS_MAP = {
    '©':'(c)'
}
var GREEK_MAP = {
    'α':'a', 'β':'b', 'γ':'g', 'δ':'d', 'ε':'e', 'ζ':'z', 'η':'h', 'θ':'8',
    'ι':'i', 'κ':'k', 'λ':'l', 'μ':'m', 'ν':'n', 'ξ':'3', 'ο':'o', 'Ï':'p',
    'ρ':'r', 'Ï':'s', 'Ï':'t', 'Ï':'y', 'Ï':'f', 'Ï':'x', 'Ï':'ps', 'Ï':'w',
    'ά':'a', 'έ':'e', 'ί':'i', 'Ï':'o', 'ύ':'y', 'ή':'h', 'Ï':'w', 'Ï':'s',
    'Ï':'i', 'ΰ':'y', 'Ï':'y', 'ΐ':'i',
    'Î':'A', 'Î':'B', 'Î':'G', 'Î':'D', 'Î':'E', 'Î':'Z', 'Î':'H', 'Î':'8',
    'Î':'I', 'Î':'K', 'Î':'L', 'Î':'M', 'Ν':'N', 'Î':'3', 'Î':'O', 'Î':'P',
    'Ρ':'R', 'Σ':'S', 'Τ':'T', 'Υ':'Y', 'Φ':'F', 'Χ':'X', 'Ψ':'PS', 'Ω':'W',
    'Î':'A', 'Î':'E', 'Î':'I', 'Î':'O', 'Î':'Y', 'Î':'H', 'Ώ':'W', 'Ϊ':'I',
    'Ϋ':'Y'
}
var TURKISH_MAP = {
    'Å':'s', 'Å':'S', 'ı':'i', 'İ':'I', 'ç':'c', 'Ã':'C', 'ü':'u', 'Ã':'U',
    'ö':'o', 'Ã':'O', 'Ä':'g', 'Ä':'G'
}
var RUSSIAN_MAP = {
    'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'Ñ':'yo', 'ж':'zh',
    'з':'z', 'и':'i', 'й':'j', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o',
    'п':'p', 'Ñ':'r', 'с':'s', 'Ñ':'t', 'Ñ':'u', 'Ñ':'f', 'Ñ':'h', 'Ñ':'c',
    'Ñ':'ch', 'Ñ':'sh', 'Ñ':'sh', 'Ñ':'', 'Ñ':'y', 'Ñ':'', 'э':'e', 'Ñ':'yu',
    'я':'ya',
    'А':'A', 'Ð':'B', 'Ð':'V', 'Ð':'G', 'Ð':'D', 'Ð':'E', 'Ё':'Yo', 'Ð':'Zh',
    'Ð':'Z', 'Ð':'I', 'Ð':'J', 'Ð':'K', 'Ð':'L', 'Ð':'M', 'Н':'N', 'Ð':'O',
    'Ð':'P', 'Ð':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'H', 'Ц':'C',
    'Ч':'Ch', 'Ш':'Sh', 'Щ':'Sh', 'Ъ':'', 'Ы':'Y', 'Ь':'', 'Э':'E', 'Ю':'Yu',
    'Я':'Ya'
}
var UKRAINIAN_MAP = {
    'Ð':'Ye', 'Ð':'I', 'Ð':'Yi', 'Ґ':'G', 'Ñ':'ye', 'Ñ':'i', 'Ñ':'yi', 'Ò':'g'
}
var CZECH_MAP = {
    'č':'c', 'ď':'d', 'Ä':'e', 'Å': 'n', 'Å':'r', 'š':'s', 'ť':'t', 'ů':'u',
    'ž':'z', 'Ä':'C', 'Ä':'D', 'Ä':'E', 'Å': 'N', 'Å':'R', 'Å':'S', 'Ť':'T',
    'Ů':'U', 'Ž':'Z'
}

var POLISH_MAP = {
    'Ä':'a', 'Ä':'c', 'Ä':'e', 'Å':'l', 'Å':'n', 'ó':'o', 'Å':'s', 'ź':'z',
    'ż':'z', 'Ä':'A', 'Ä':'C', 'Ä':'e', 'Ł':'L', 'Å':'N', 'Ã':'o', 'Å':'S',
    'Ź':'Z', 'Ż':'Z'
}

var LATVIAN_MAP = {
    'ā':'a', 'č':'c', 'Ä':'e', 'ģ':'g', 'ī':'i', 'ķ':'k', 'ļ':'l', 'Å':'n',
    'š':'s', 'ū':'u', 'ž':'z', 'Ä':'A', 'Ä':'C', 'Ä':'E', 'Ģ':'G', 'Ī':'i',
    'Ķ':'k', 'Ļ':'L', 'Å':'N', 'Å':'S', 'Ū':'u', 'Ž':'Z'
}

var ALL_DOWNCODE_MAPS=new Array()
ALL_DOWNCODE_MAPS[0]=LATIN_MAP
ALL_DOWNCODE_MAPS[1]=LATIN_SYMBOLS_MAP
ALL_DOWNCODE_MAPS[2]=GREEK_MAP
ALL_DOWNCODE_MAPS[3]=TURKISH_MAP
ALL_DOWNCODE_MAPS[4]=RUSSIAN_MAP
ALL_DOWNCODE_MAPS[5]=UKRAINIAN_MAP
ALL_DOWNCODE_MAPS[6]=CZECH_MAP
ALL_DOWNCODE_MAPS[7]=POLISH_MAP
ALL_DOWNCODE_MAPS[8]=LATVIAN_MAP

var Downcoder = new Object();
Downcoder.Initialize = function()
{
    if (Downcoder.map) // already made
        return ;
    Downcoder.map ={}
    Downcoder.chars = '' ;
    for(var i in ALL_DOWNCODE_MAPS)
    {
        var lookup = ALL_DOWNCODE_MAPS[i]
        for (var c in lookup)
        {
            Downcoder.map[c] = lookup[c] ;
            Downcoder.chars += c ;
        }
     }
    Downcoder.regex = new RegExp('[' + Downcoder.chars + ']|[^' + Downcoder.chars + ']+','g') ;
}

downcode= function( slug )
{
    Downcoder.Initialize() ;
    var downcoded =""
    var pieces = slug.match(Downcoder.regex);
    if(pieces)
    {
        for (var i = 0 ; i < pieces.length ; i++)
        {
            if (pieces[i].length == 1)
            {
                var mapped = Downcoder.map[pieces[i]] ;
                if (mapped != null)
                {
                    downcoded+=mapped;
                    continue ;
                }
            }
            downcoded+=pieces[i];
        }
    }
    else
    {
        downcoded = slug;
    }
    return downcoded;
}


function URLify(s, num_chars) {
    // changes, e.g., "Petty theft" to "petty_theft"
    // remove all these words from the string before urlifying
    s = downcode(s);
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for", "from",
                  "is", "in", "into", "like", "of", "off", "on", "onto", "per",
                  "since", "than", "the", "this", "that", "to", "up", "via",
                  "with"];
    r = new RegExp('\\b(' + removelist.join('|') + ')\\b', 'gi');
    s = s.replace(r, '');
    // if downcode doesn't hit, the char will be stripped here
    s = s.replace(/[^-\w\s]/g, '');  // remove unneeded chars
    s = s.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
    s = s.replace(/[-\s]+/g, '-');   // convert spaces to hyphens
    s = s.toLowerCase();             // convert to lowercase
    return s.substring(0, num_chars);// trim to first num_chars chars
}
""").decode('iso-8859-15')

URLIFY_DJANGO_WIKI = ("""
  // Replacement of django's URLify that doesn't remove any words.
  function URLify(s, num_chars) {
      s = downcode(s);
      removelist = [];
      r = new RegExp('\\b(' + removelist.join('|') + ')\\b', 'gi');
      s = s.replace(r, '');
      // if downcode doesn't hit, the char will be stripped here
      s = s.replace(/[^-\w\s]/g, '');  // remove unneeded chars
      s = s.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
      s = s.replace(/[-\s]+/g, '-');   // convert spaces to hyphens
      s = s.toLowerCase();             // convert to lowercase
      return s.substring(0, num_chars);// trim to first num_chars chars
  }

  function slugify(e) {
      slug = URLify(e, 50);
      wikislug = slug.replace(/\-/g, " ");
      wikislug = wikislug.replace(/\w\S*/gi, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1);});
      wikislug = wikislug.replace(/\s*/g, "");
      return wikislug;
  }
""").decode('iso-8859-15')
