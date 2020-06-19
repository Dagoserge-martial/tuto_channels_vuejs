# tuto_channels_vuejs
 
# select2

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-beta.1/css/select2.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-beta.1/js/select2.min.js"></script>
    <script>
        $(document).ready(function(){
            var sportlist = [
                "crickey","vollleyball","Rubby", "Tennis","Baseball"
            ];
            var isoCountries = [

                {
                    "name": "Afghanistan",
                    "code": "AF"
                },
                {
                    "name": "Åland Islands",
                    "code": "AX"
                },
                {
                    "name": "Albania",
                    "code": "AL"
                },
                {
                    "name": "Algeria",
                    "code": "DZ"
                },
                {
                    "name": "American Samoa",
                    "code": "AS"
                },
                {
                    "name": "AndorrA",
                    "code": "AD"
                },
                {
                    "name": "Angola",
                    "code": "AO"
                },
                {
                    "name": "Anguilla",
                    "code": "AI"
                },
                {
                    "name": "Antarctica",
                    "code": "AQ"
                },
                {
                    "name": "Antigua and Barbuda",
                    "code": "AG"
                },
                {
                    "name": "Argentina",
                    "code": "AR"
                },
                {
                    "name": "Armenia",
                    "code": "AM"
                },
                {
                    "name": "Aruba",
                    "code": "AW"
                },
                {
                    "name": "Australia",
                    "code": "AU"
                },
                {
                    "name": "Austria",
                    "code": "AT"
                },
                {
                    "name": "Azerbaijan",
                    "code": "AZ"
                },
                {
                    "name": "Bahamas",
                    "code": "BS"
                },
                {
                    "name": "Bahrain",
                    "code": "BH"
                },
                {
                    "name": "Bangladesh",
                    "code": "BD"
                },
                {
                    "name": "Barbados",
                    "code": "BB"
                },
                {
                    "name": "Belarus",
                    "code": "BY"
                },
                {
                    "name": "Belgium",
                    "code": "BE"
                },
                {
                    "name": "Belize",
                    "code": "BZ"
                },
                {
                    "name": "Benin",
                    "code": "BJ"
                },
                {
                    "name": "Bermuda",
                    "code": "BM"
                },
                {
                    "name": "Bhutan",
                    "code": "BT"
                },
                {
                    "name": "Bolivia",
                    "code": "BO"
                },
                {
                    "name": "Bosnia and Herzegovina",
                    "code": "BA"
                },
                {
                    "name": "Botswana",
                    "code": "BW"
                },
                {
                    "name": "Bouvet Island",
                    "code": "BV"
                },
                {
                    "name": "Brazil",
                    "code": "BR"
                },
                {
                    "name": "British Indian Ocean Territory",
                    "code": "IO"
                },
                {
                    "name": "Brunei Darussalam",
                    "code": "BN"
                },
                {
                    "name": "Bulgaria",
                    "code": "BG"
                },
                {
                    "name": "Burkina Faso",
                    "code": "BF"
                },
                {
                    "name": "Burundi",
                    "code": "BI"
                },
                {
                    "name": "Cambodia",
                    "code": "KH"
                },
                {
                    "name": "Cameroon",
                    "code": "CM"
                },
                {
                    "name": "Canada",
                    "code": "CA"
                },
                {
                    "name": "Cape Verde",
                    "code": "CV"
                },
                {
                    "name": "Cayman Islands",
                    "code": "KY"
                },
                {
                    "name": "Central African Republic",
                    "code": "CF"
                },
                {
                    "name": "Chad",
                    "code": "TD"
                },
                {
                    "name": "Chile",
                    "code": "CL"
                },
                {
                    "name": "China",
                    "code": "CN"
                },
                {
                    "name": "Christmas Island",
                    "code": "CX"
                },
                {
                    "name": "Cocos (Keeling) Islands",
                    "code": "CC"
                },
                {
                    "name": "Colombia",
                    "code": "CO"
                },
                {
                    "name": "Comoros",
                    "code": "KM"
                },
                {
                    "name": "Congo",
                    "code": "CG"
                },
                {
                    "name": "Congo, The Democratic Republic of the",
                    "code": "CD"
                },
                {
                    "name": "Cook Islands",
                    "code": "CK"
                },
                {
                    "name": "Costa Rica",
                    "code": "CR"
                },
                {
                    "name": "Cote D\"Ivoire",
                    "code": "CI"
                },
                {
                    "name": "Croatia",
                    "code": "HR"
                },
                {
                    "name": "Cuba",
                    "code": "CU"
                },
                {
                    "name": "Cyprus",
                    "code": "CY"
                },
                {
                    "name": "Czech Republic",
                    "code": "CZ"
                },
                {
                    "name": "Denmark",
                    "code": "DK"
                },
                {
                    "name": "Djibouti",
                    "code": "DJ"
                },
                {
                    "name": "Dominica",
                    "code": "DM"
                },
                {
                    "name": "Dominican Republic",
                    "code": "DO"
                },
                {
                    "name": "Ecuador",
                    "code": "EC"
                },
                {
                    "name": "Egypt",
                    "code": "EG"
                },
                {
                    "name": "El Salvador",
                    "code": "SV"
                },
                {
                    "name": "Equatorial Guinea",
                    "code": "GQ"
                },
                {
                    "name": "Eritrea",
                    "code": "ER"
                },
                {
                    "name": "Estonia",
                    "code": "EE"
                },
                {
                    "name": "Ethiopia",
                    "code": "ET"
                },
                {
                    "name": "Falkland Islands (Malvinas)",
                    "code": "FK"
                },
                {
                    "name": "Faroe Islands",
                    "code": "FO"
                },
                {
                    "name": "Fiji",
                    "code": "FJ"
                },
                {
                    "name": "Finland",
                    "code": "FI"
                },
                {
                    "name": "France",
                    "code": "FR"
                },
                {
                    "name": "French Guiana",
                    "code": "GF"
                },
                {
                    "name": "French Polynesia",
                    "code": "PF"
                },
                {
                    "name": "French Southern Territories",
                    "code": "TF"
                },
                {
                    "name": "Gabon",
                    "code": "GA"
                },
                {
                    "name": "Gambia",
                    "code": "GM"
                },
                {
                    "name": "Georgia",
                    "code": "GE"
                },
                {
                    "name": "Germany",
                    "code": "DE"
                },
                {
                    "name": "Ghana",
                    "code": "GH"
                },
                {
                    "name": "Gibraltar",
                    "code": "GI"
                },
                {
                    "name": "Greece",
                    "code": "GR"
                },
                {
                    "name": "Greenland",
                    "code": "GL"
                },
                {
                    "name": "Grenada",
                    "code": "GD"
                },
                {
                    "name": "Guadeloupe",
                    "code": "GP"
                },
                {
                    "name": "Guam",
                    "code": "GU"
                },
                {
                    "name": "Guatemala",
                    "code": "GT"
                },
                {
                    "name": "Guernsey",
                    "code": "GG"
                },
                {
                    "name": "Guinea",
                    "code": "GN"
                },
                {
                    "name": "Guinea-Bissau",
                    "code": "GW"
                },
                {
                    "name": "Guyana",
                    "code": "GY"
                },
                {
                    "name": "Haiti",
                    "code": "HT"
                },
                {
                    "name": "Heard Island and Mcdonald Islands",
                    "code": "HM"
                },
                {
                    "name": "Holy See (Vatican City State)",
                    "code": "VA"
                },
                {
                    "name": "Honduras",
                    "code": "HN"
                },
                {
                    "name": "Hong Kong",
                    "code": "HK"
                },
                {
                    "name": "Hungary",
                    "code": "HU"
                },
                {
                    "name": "Iceland",
                    "code": "IS"
                },
                {
                    "name": "India",
                    "code": "IN"
                },
                {
                    "name": "Indonesia",
                    "code": "ID"
                },
                {
                    "name": "Iran, Islamic Republic Of",
                    "code": "IR"
                },
                {
                    "name": "Iraq",
                    "code": "IQ"
                },
                {
                    "name": "Ireland",
                    "code": "IE"
                },
                {
                    "name": "Isle of Man",
                    "code": "IM"
                },
                {
                    "name": "Israel",
                    "code": "IL"
                },
                {
                    "name": "Italy",
                    "code": "IT"
                },
                {
                    "name": "Jamaica",
                    "code": "JM"
                },
                {
                    "name": "Japan",
                    "code": "JP"
                },
                {
                    "name": "Jersey",
                    "code": "JE"
                },
                {
                    "name": "Jordan",
                    "code": "JO"
                },
                {
                    "name": "Kazakhstan",
                    "code": "KZ"
                },
                {
                    "name": "Kenya",
                    "code": "KE"
                },
                {
                    "name": "Kiribati",
                    "code": "KI"
                },
                {
                    "name": "Korea, Democratic People\"S Republic of",
                    "code": "KP"
                },
                {
                    "name": "Korea, Republic of",
                    "code": "KR"
                },
                {
                    "name": "Kuwait",
                    "code": "KW"
                },
                {
                    "name": "Kyrgyzstan",
                    "code": "KG"
                },
                {
                    "name": "Lao People\"S Democratic Republic",
                    "code": "LA"
                },
                {
                    "name": "Latvia",
                    "code": "LV"
                },
                {
                    "name": "Lebanon",
                    "code": "LB"
                },
                {
                    "name": "Lesotho",
                    "code": "LS"
                },
                {
                    "name": "Liberia",
                    "code": "LR"
                },
                {
                    "name": "Libyan Arab Jamahiriya",
                    "code": "LY"
                },
                {
                    "name": "Liechtenstein",
                    "code": "LI"
                },
                {
                    "name": "Lithuania",
                    "code": "LT"
                },
                {
                    "name": "Luxembourg",
                    "code": "LU"
                },
                {
                    "name": "Macao",
                    "code": "MO"
                },
                {
                    "name": "Macedonia, The Former Yugoslav Republic of",
                    "code": "MK"
                },
                {
                    "name": "Madagascar",
                    "code": "MG"
                },
                {
                    "name": "Malawi",
                    "code": "MW"
                },
                {
                    "name": "Malaysia",
                    "code": "MY"
                },
                {
                    "name": "Maldives",
                    "code": "MV"
                },
                {
                    "name": "Mali",
                    "code": "ML"
                },
                {
                    "name": "Malta",
                    "code": "MT"
                },
                {
                    "name": "Marshall Islands",
                    "code": "MH"
                },
                {
                    "name": "Martinique",
                    "code": "MQ"
                },
                {
                    "name": "Mauritania",
                    "code": "MR"
                },
                {
                    "name": "Mauritius",
                    "code": "MU"
                },
                {
                    "name": "Mayotte",
                    "code": "YT"
                },
                {
                    "name": "Mexico",
                    "code": "MX"
                },
                {
                    "name": "Micronesia, Federated States of",
                    "code": "FM"
                },
                {
                    "name": "Moldova, Republic of",
                    "code": "MD"
                },
                {
                    "name": "Monaco",
                    "code": "MC"
                },
                {
                    "name": "Mongolia",
                    "code": "MN"
                },
                {
                    "name": "Montserrat",
                    "code": "MS"
                },
                {
                    "name": "Morocco",
                    "code": "MA"
                },
                {
                    "name": "Mozambique",
                    "code": "MZ"
                },
                {
                    "name": "Myanmar",
                    "code": "MM"
                },
                {
                    "name": "Namibia",
                    "code": "NA"
                },
                {
                    "name": "Nauru",
                    "code": "NR"
                },
                {
                    "name": "Nepal",
                    "code": "NP"
                },
                {
                    "name": "Netherlands",
                    "code": "NL"
                },
                {
                    "name": "Netherlands Antilles",
                    "code": "AN"
                },
                {
                    "name": "New Caledonia",
                    "code": "NC"
                },
                {
                    "name": "New Zealand",
                    "code": "NZ"
                },
                {
                    "name": "Nicaragua",
                    "code": "NI"
                },
                {
                    "name": "Niger",
                    "code": "NE"
                },
                {
                    "name": "Nigeria",
                    "code": "NG"
                },
                {
                    "name": "Niue",
                    "code": "NU"
                },
                {
                    "name": "Norfolk Island",
                    "code": "NF"
                },
                {
                    "name": "Northern Mariana Islands",
                    "code": "MP"
                },
                {
                    "name": "Norway",
                    "code": "NO"
                },
                {
                    "name": "Oman",
                    "code": "OM"
                },
                {
                    "name": "Pakistan",
                    "code": "PK"
                },
                {
                    "name": "Palau",
                    "code": "PW"
                },
                {
                    "name": "Palestinian Territory, Occupied",
                    "code": "PS"
                },
                {
                    "name": "Panama",
                    "code": "PA"
                },
                {
                    "name": "Papua New Guinea",
                    "code": "PG"
                },
                {
                    "name": "Paraguay",
                    "code": "PY"
                },
                {
                    "name": "Peru",
                    "code": "PE"
                },
                {
                    "name": "Philippines",
                    "code": "PH"
                },
                {
                    "name": "Pitcairn",
                    "code": "PN"
                },
                {
                    "name": "Poland",
                    "code": "PL"
                },
                {
                    "name": "Portugal",
                    "code": "PT"
                },
                {
                    "name": "Puerto Rico",
                    "code": "PR"
                },
                {
                    "name": "Qatar",
                    "code": "QA"
                },
                {
                    "name": "Reunion",
                    "code": "RE"
                },
                {
                    "name": "Romania",
                    "code": "RO"
                },
                {
                    "name": "Russian Federation",
                    "code": "RU"
                },
                {
                    "name": "RWANDA",
                    "code": "RW"
                },
                {
                    "name": "Saint Helena",
                    "code": "SH"
                },
                {
                    "name": "Saint Kitts and Nevis",
                    "code": "KN"
                },
                {
                    "name": "Saint Lucia",
                    "code": "LC"
                },
                {
                    "name": "Saint Pierre and Miquelon",
                    "code": "PM"
                },
                {
                    "name": "Saint Vincent and the Grenadines",
                    "code": "VC"
                },
                {
                    "name": "Samoa",
                    "code": "WS"
                },
                {
                    "name": "San Marino",
                    "code": "SM"
                },
                {
                    "name": "Sao Tome and Principe",
                    "code": "ST"
                },
                {
                    "name": "Saudi Arabia",
                    "code": "SA"
                },
                {
                    "name": "Senegal",
                    "code": "SN"
                },
                {
                    "name": "Serbia and Montenegro",
                    "code": "CS"
                },
                {
                    "name": "Seychelles",
                    "code": "SC"
                },
                {
                    "name": "Sierra Leone",
                    "code": "SL"
                },
                {
                    "name": "Singapore",
                    "code": "SG"
                },
                {
                    "name": "Slovakia",
                    "code": "SK"
                },
                {
                    "name": "Slovenia",
                    "code": "SI"
                },
                {
                    "name": "Solomon Islands",
                    "code": "SB"
                },
                {
                    "name": "Somalia",
                    "code": "SO"
                },
                {
                    "name": "South Africa",
                    "code": "ZA"
                },
                {
                    "name": "South Georgia and the South Sandwich Islands",
                    "code": "GS"
                },
                {
                    "name": "Spain",
                    "code": "ES"
                },
                {
                    "name": "Sri Lanka",
                    "code": "LK"
                },
                {
                    "name": "Sudan",
                    "code": "SD"
                },
                {
                    "name": "Suriname",
                    "code": "SR"
                },
                {
                    "name": "Svalbard and Jan Mayen",
                    "code": "SJ"
                },
                {
                    "name": "Swaziland",
                    "code": "SZ"
                },
                {
                    "name": "Sweden",
                    "code": "SE"
                },
                {
                    "name": "Switzerland",
                    "code": "CH"
                },
                {
                    "name": "Syrian Arab Republic",
                    "code": "SY"
                },
                {
                    "name": "Taiwan, Province of China",
                    "code": "TW"
                },
                {
                    "name": "Tajikistan",
                    "code": "TJ"
                },
                {
                    "name": "Tanzania, United Republic of",
                    "code": "TZ"
                },
                {
                    "name": "Thailand",
                    "code": "TH"
                },
                {
                    "name": "Timor-Leste",
                    "code": "TL"
                },
                {
                    "name": "Togo",
                    "code": "TG"
                },
                {
                    "name": "Tokelau",
                    "code": "TK"
                },
                {
                    "name": "Tonga",
                    "code": "TO"
                },
                {
                    "name": "Trinidad and Tobago",
                    "code": "TT"
                },
                {
                    "name": "Tunisia",
                    "code": "TN"
                },
                {
                    "name": "Turkey",
                    "code": "TR"
                },
                {
                    "name": "Turkmenistan",
                    "code": "TM"
                },
                {
                    "name": "Turks and Caicos Islands",
                    "code": "TC"
                },
                {
                    "name": "Tuvalu",
                    "code": "TV"
                },
                {
                    "name": "Uganda",
                    "code": "UG"
                },
                {
                    "name": "Ukraine",
                    "code": "UA"
                },
                {
                    "name": "United Arab Emirates",
                    "code": "AE"
                },
                {
                    "name": "United Kingdom",
                    "code": "GB"
                },
                {
                    "name": "United States",
                    "code": "US"
                },
                {
                    "name": "United States Minor Outlying Islands",
                    "code": "UM"
                },
                {
                    "name": "Uruguay",
                    "code": "UY"
                },
                {
                    "name": "Uzbekistan",
                    "code": "UZ"
                },
                {
                    "name": "Vanuatu",
                    "code": "VU"
                },
                {
                    "name": "Venezuela",
                    "code": "VE"
                },
                {
                    "name": "Viet Nam",
                    "code": "VN"
                },
                {
                    "name": "Virgin Islands, British",
                    "code": "VG"
                },
                {
                    "name": "Virgin Islands, U.S.",
                    "code": "VI"
                },
                {
                    "name": "Wallis and Futuna",
                    "code": "WF"
                },
                {
                    "name": "Western Sahara",
                    "code": "EH"
                },
                {
                    "name": "Yemen",
                    "code": "YE"
                },
                {
                    "name": "Zambia",
                    "code": "ZM"
                },
                {
                    "name": "Zimbabwe",
                    "code": "ZW"
                }
            ];

            $("#country").select2({
                data:isoCountries
            });

            $("[name='country']").select2({
            placeholder: "Select a country",
            data: isoCountries
        });
        console.log(isoCountries[0].code)
        })
    </script>
</head>
<body>
    <div id="apps">
        <h1> Select 2 ${selected}</h1>
        <hr>
        <select v-model='selected' id="country">
            <option value="" selected hidden disabled>-- Select Country --</option>
            <option @click='choix(CI)' v-for='pay in pays' v-bind:value="pay.code">${pay.name}</option>
        </select>
        <span>Sélectionné : ${selected}</span><br><br>
        
        
        <select v-model="selected">
            <option v-for="option in options" v-bind:value="option.value">
              ${ option.text }
            </option>
          </select>
          <span>Sélectionné : ${ selected }</span>
    </div>
<!-- 
    <select name="countryCode" id="">
        <option data-countryCode="GB" value="44" Selected>UK (+44)</option>
        <option data-countryCode="US" value="1">USA (+1)</option>
        <optgroup label="Other countries">
            <option data-countryCode="DZ" value="213">Algeria (+213)</option>
            <option data-countryCode="AD" value="376">Andorra (+376)</option>
            <option data-countryCode="AO" value="244">Angola (+244)</option>
            <option data-countryCode="AI" value="1264">Anguilla (+1264)</option>
            <option data-countryCode="AG" value="1268">Antigua &amp; Barbuda (+1268)</option>
            <option data-countryCode="AR" value="54">Argentina (+54)</option>
            <option data-countryCode="AM" value="374">Armenia (+374)</option>
            <option data-countryCode="AW" value="297">Aruba (+297)</option>
            <option data-countryCode="AU" value="61">Australia (+61)</option>
            <option data-countryCode="AT" value="43">Austria (+43)</option>
            <option data-countryCode="AZ" value="994">Azerbaijan (+994)</option>
            <option data-countryCode="BS" value="1242">Bahamas (+1242)</option>
            <option data-countryCode="BH" value="973">Bahrain (+973)</option>
            <option data-countryCode="BD" value="880">Bangladesh (+880)</option>
            <option data-countryCode="BB" value="1246">Barbados (+1246)</option>
            <option data-countryCode="BY" value="375">Belarus (+375)</option>
            <option data-countryCode="BE" value="32">Belgium (+32)</option>
            <option data-countryCode="BZ" value="501">Belize (+501)</option>
            <option data-countryCode="BJ" value="229">Benin (+229)</option>
            <option data-countryCode="BM" value="1441">Bermuda (+1441)</option>
            <option data-countryCode="BT" value="975">Bhutan (+975)</option>
            <option data-countryCode="BO" value="591">Bolivia (+591)</option>
            <option data-countryCode="BA" value="387">Bosnia Herzegovina (+387)</option>
            <option data-countryCode="BW" value="267">Botswana (+267)</option>
            <option data-countryCode="BR" value="55">Brazil (+55)</option>
            <option data-countryCode="BN" value="673">Brunei (+673)</option>
            <option data-countryCode="BG" value="359">Bulgaria (+359)</option>
            <option data-countryCode="BF" value="226">Burkina Faso (+226)</option>
            <option data-countryCode="BI" value="257">Burundi (+257)</option>
            <option data-countryCode="KH" value="855">Cambodia (+855)</option>
            <option data-countryCode="CM" value="237">Cameroon (+237)</option>
            <option data-countryCode="CA" value="1">Canada (+1)</option>
            <option data-countryCode="CV" value="238">Cape Verde Islands (+238)</option>
            <option data-countryCode="KY" value="1345">Cayman Islands (+1345)</option>
            <option data-countryCode="CF" value="236">Central African Republic (+236)</option>
            <option data-countryCode="CL" value="56">Chile (+56)</option>
            <option data-countryCode="CN" value="86">China (+86)</option>
            <option data-countryCode="CO" value="57">Colombia (+57)</option>
            <option data-countryCode="KM" value="269">Comoros (+269)</option>
            <option data-countryCode="CG" value="242">Congo (+242)</option>
            <option data-countryCode="CK" value="682">Cook Islands (+682)</option>
            <option data-countryCode="CR" value="506">Costa Rica (+506)</option>
            <option data-countryCode="HR" value="385">Croatia (+385)</option>
            <option data-countryCode="CU" value="53">Cuba (+53)</option>
            <option data-countryCode="CY" value="90392">Cyprus North (+90392)</option>
            <option data-countryCode="CY" value="357">Cyprus South (+357)</option>
            <option data-countryCode="CZ" value="42">Czech Republic (+42)</option>
            <option data-countryCode="DK" value="45">Denmark (+45)</option>
            <option data-countryCode="DJ" value="253">Djibouti (+253)</option>
            <option data-countryCode="DM" value="1809">Dominica (+1809)</option>
            <option data-countryCode="DO" value="1809">Dominican Republic (+1809)</option>
            <option data-countryCode="EC" value="593">Ecuador (+593)</option>
            <option data-countryCode="EG" value="20">Egypt (+20)</option>
            <option data-countryCode="SV" value="503">El Salvador (+503)</option>
            <option data-countryCode="GQ" value="240">Equatorial Guinea (+240)</option>
            <option data-countryCode="ER" value="291">Eritrea (+291)</option>
            <option data-countryCode="EE" value="372">Estonia (+372)</option>
            <option data-countryCode="ET" value="251">Ethiopia (+251)</option>
            <option data-countryCode="FK" value="500">Falkland Islands (+500)</option>
            <option data-countryCode="FO" value="298">Faroe Islands (+298)</option>
            <option data-countryCode="FJ" value="679">Fiji (+679)</option>
            <option data-countryCode="FI" value="358">Finland (+358)</option>
            <option data-countryCode="FR" value="33">France (+33)</option>
            <option data-countryCode="GF" value="594">French Guiana (+594)</option>
            <option data-countryCode="PF" value="689">French Polynesia (+689)</option>
            <option data-countryCode="GA" value="241">Gabon (+241)</option>
            <option data-countryCode="GM" value="220">Gambia (+220)</option>
            <option data-countryCode="GE" value="7880">Georgia (+7880)</option>
            <option data-countryCode="DE" value="49">Germany (+49)</option>
            <option data-countryCode="GH" value="233">Ghana (+233)</option>
            <option data-countryCode="GI" value="350">Gibraltar (+350)</option>
            <option data-countryCode="GR" value="30">Greece (+30)</option>
            <option data-countryCode="GL" value="299">Greenland (+299)</option>
            <option data-countryCode="GD" value="1473">Grenada (+1473)</option>
            <option data-countryCode="GP" value="590">Guadeloupe (+590)</option>
            <option data-countryCode="GU" value="671">Guam (+671)</option>
            <option data-countryCode="GT" value="502">Guatemala (+502)</option>
            <option data-countryCode="GN" value="224">Guinea (+224)</option>
            <option data-countryCode="GW" value="245">Guinea - Bissau (+245)</option>
            <option data-countryCode="GY" value="592">Guyana (+592)</option>
            <option data-countryCode="HT" value="509">Haiti (+509)</option>
            <option data-countryCode="HN" value="504">Honduras (+504)</option>
            <option data-countryCode="HK" value="852">Hong Kong (+852)</option>
            <option data-countryCode="HU" value="36">Hungary (+36)</option>
            <option data-countryCode="IS" value="354">Iceland (+354)</option>
            <option data-countryCode="IN" value="91">India (+91)</option>
            <option data-countryCode="ID" value="62">Indonesia (+62)</option>
            <option data-countryCode="IR" value="98">Iran (+98)</option>
            <option data-countryCode="IQ" value="964">Iraq (+964)</option>
            <option data-countryCode="IE" value="353">Ireland (+353)</option>
            <option data-countryCode="IL" value="972">Israel (+972)</option>
            <option data-countryCode="IT" value="39">Italy (+39)</option>
            <option data-countryCode="JM" value="1876">Jamaica (+1876)</option>
            <option data-countryCode="JP" value="81">Japan (+81)</option>
            <option data-countryCode="JO" value="962">Jordan (+962)</option>
            <option data-countryCode="KZ" value="7">Kazakhstan (+7)</option>
            <option data-countryCode="KE" value="254">Kenya (+254)</option>
            <option data-countryCode="KI" value="686">Kiribati (+686)</option>
            <option data-countryCode="KP" value="850">Korea North (+850)</option>
            <option data-countryCode="KR" value="82">Korea South (+82)</option>
            <option data-countryCode="KW" value="965">Kuwait (+965)</option>
            <option data-countryCode="KG" value="996">Kyrgyzstan (+996)</option>
            <option data-countryCode="LA" value="856">Laos (+856)</option>
            <option data-countryCode="LV" value="371">Latvia (+371)</option>
            <option data-countryCode="LB" value="961">Lebanon (+961)</option>
            <option data-countryCode="LS" value="266">Lesotho (+266)</option>
            <option data-countryCode="LR" value="231">Liberia (+231)</option>
            <option data-countryCode="LY" value="218">Libya (+218)</option>
            <option data-countryCode="LI" value="417">Liechtenstein (+417)</option>
            <option data-countryCode="LT" value="370">Lithuania (+370)</option>
            <option data-countryCode="LU" value="352">Luxembourg (+352)</option>
            <option data-countryCode="MO" value="853">Macao (+853)</option>
            <option data-countryCode="MK" value="389">Macedonia (+389)</option>
            <option data-countryCode="MG" value="261">Madagascar (+261)</option>
            <option data-countryCode="MW" value="265">Malawi (+265)</option>
            <option data-countryCode="MY" value="60">Malaysia (+60)</option>
            <option data-countryCode="MV" value="960">Maldives (+960)</option>
            <option data-countryCode="ML" value="223">Mali (+223)</option>
            <option data-countryCode="MT" value="356">Malta (+356)</option>
            <option data-countryCode="MH" value="692">Marshall Islands (+692)</option>
            <option data-countryCode="MQ" value="596">Martinique (+596)</option>
            <option data-countryCode="MR" value="222">Mauritania (+222)</option>
            <option data-countryCode="YT" value="269">Mayotte (+269)</option>
            <option data-countryCode="MX" value="52">Mexico (+52)</option>
            <option data-countryCode="FM" value="691">Micronesia (+691)</option>
            <option data-countryCode="MD" value="373">Moldova (+373)</option>
            <option data-countryCode="MC" value="377">Monaco (+377)</option>
            <option data-countryCode="MN" value="976">Mongolia (+976)</option>
            <option data-countryCode="MS" value="1664">Montserrat (+1664)</option>
            <option data-countryCode="MA" value="212">Morocco (+212)</option>
            <option data-countryCode="MZ" value="258">Mozambique (+258)</option>
            <option data-countryCode="MN" value="95">Myanmar (+95)</option>
            <option data-countryCode="NA" value="264">Namibia (+264)</option>
            <option data-countryCode="NR" value="674">Nauru (+674)</option>
            <option data-countryCode="NP" value="977">Nepal (+977)</option>
            <option data-countryCode="NL" value="31">Netherlands (+31)</option>
            <option data-countryCode="NC" value="687">New Caledonia (+687)</option>
            <option data-countryCode="NZ" value="64">New Zealand (+64)</option>
            <option data-countryCode="NI" value="505">Nicaragua (+505)</option>
            <option data-countryCode="NE" value="227">Niger (+227)</option>
            <option data-countryCode="NG" value="234">Nigeria (+234)</option>
            <option data-countryCode="NU" value="683">Niue (+683)</option>
            <option data-countryCode="NF" value="672">Norfolk Islands (+672)</option>
            <option data-countryCode="NP" value="670">Northern Marianas (+670)</option>
            <option data-countryCode="NO" value="47">Norway (+47)</option>
            <option data-countryCode="OM" value="968">Oman (+968)</option>
            <option data-countryCode="PW" value="680">Palau (+680)</option>
            <option data-countryCode="PA" value="507">Panama (+507)</option>
            <option data-countryCode="PG" value="675">Papua New Guinea (+675)</option>
            <option data-countryCode="PY" value="595">Paraguay (+595)</option>
            <option data-countryCode="PE" value="51">Peru (+51)</option>
            <option data-countryCode="PH" value="63">Philippines (+63)</option>
            <option data-countryCode="PL" value="48">Poland (+48)</option>
            <option data-countryCode="PT" value="351">Portugal (+351)</option>
            <option data-countryCode="PR" value="1787">Puerto Rico (+1787)</option>
            <option data-countryCode="QA" value="974">Qatar (+974)</option>
            <option data-countryCode="RE" value="262">Reunion (+262)</option>
            <option data-countryCode="RO" value="40">Romania (+40)</option>
            <option data-countryCode="RU" value="7">Russia (+7)</option>
            <option data-countryCode="RW" value="250">Rwanda (+250)</option>
            <option data-countryCode="SM" value="378">San Marino (+378)</option>
            <option data-countryCode="ST" value="239">Sao Tome &amp; Principe (+239)</option>
            <option data-countryCode="SA" value="966">Saudi Arabia (+966)</option>
            <option data-countryCode="SN" value="221">Senegal (+221)</option>
            <option data-countryCode="CS" value="381">Serbia (+381)</option>
            <option data-countryCode="SC" value="248">Seychelles (+248)</option>
            <option data-countryCode="SL" value="232">Sierra Leone (+232)</option>
            <option data-countryCode="SG" value="65">Singapore (+65)</option>
            <option data-countryCode="SK" value="421">Slovak Republic (+421)</option>
            <option data-countryCode="SI" value="386">Slovenia (+386)</option>
            <option data-countryCode="SB" value="677">Solomon Islands (+677)</option>
            <option data-countryCode="SO" value="252">Somalia (+252)</option>
            <option data-countryCode="ZA" value="27">South Africa (+27)</option>
            <option data-countryCode="ES" value="34">Spain (+34)</option>
            <option data-countryCode="LK" value="94">Sri Lanka (+94)</option>
            <option data-countryCode="SH" value="290">St. Helena (+290)</option>
            <option data-countryCode="KN" value="1869">St. Kitts (+1869)</option>
            <option data-countryCode="SC" value="1758">St. Lucia (+1758)</option>
            <option data-countryCode="SD" value="249">Sudan (+249)</option>
            <option data-countryCode="SR" value="597">Suriname (+597)</option>
            <option data-countryCode="SZ" value="268">Swaziland (+268)</option>
            <option data-countryCode="SE" value="46">Sweden (+46)</option>
            <option data-countryCode="CH" value="41">Switzerland (+41)</option>
            <option data-countryCode="SI" value="963">Syria (+963)</option>
            <option data-countryCode="TW" value="886">Taiwan (+886)</option>
            <option data-countryCode="TJ" value="7">Tajikstan (+7)</option>
            <option data-countryCode="TH" value="66">Thailand (+66)</option>
            <option data-countryCode="TG" value="228">Togo (+228)</option>
            <option data-countryCode="TO" value="676">Tonga (+676)</option>
            <option data-countryCode="TT" value="1868">Trinidad &amp; Tobago (+1868)</option>
            <option data-countryCode="TN" value="216">Tunisia (+216)</option>
            <option data-countryCode="TR" value="90">Turkey (+90)</option>
            <option data-countryCode="TM" value="7">Turkmenistan (+7)</option>
            <option data-countryCode="TM" value="993">Turkmenistan (+993)</option>
            <option data-countryCode="TC" value="1649">Turks &amp; Caicos Islands (+1649)</option>
            <option data-countryCode="TV" value="688">Tuvalu (+688)</option>
            <option data-countryCode="UG" value="256">Uganda (+256)</option>
            <!-- <option data-countryCode="GB" value="44">UK (+44)</option> -->
            <!-- <option data-countryCode="UA" value="380">Ukraine (+380)</option>
            <option data-countryCode="AE" value="971">United Arab Emirates (+971)</option>
            <option data-countryCode="UY" value="598">Uruguay (+598)</option> -->
            <!-- <option data-countryCode="US" value="1">USA (+1)</option> -->
            <!-- <option data-countryCode="UZ" value="7">Uzbekistan (+7)</option>
            <option data-countryCode="VU" value="678">Vanuatu (+678)</option>
            <option data-countryCode="VA" value="379">Vatican City (+379)</option>
            <option data-countryCode="VE" value="58">Venezuela (+58)</option>
            <option data-countryCode="VN" value="84">Vietnam (+84)</option>
            <option data-countryCode="VG" value="84">Virgin Islands - British (+1284)</option>
            <option data-countryCode="VI" value="84">Virgin Islands - US (+1340)</option>
            <option data-countryCode="WF" value="681">Wallis &amp; Futuna (+681)</option>
            <option data-countryCode="YE" value="969">Yemen (North)(+969)</option>
            <option data-countryCode="YE" value="967">Yemen (South)(+967)</option>
            <option data-countryCode="ZM" value="260">Zambia (+260)</option>
            <option data-countryCode="ZW" value="263">Zimbabwe (+263)</option>
        </optgroup>
    </select> --> 

    <!-- <img src="https://www.countryflags.io/ci/flat/64.png">

    <img src="https://www.countryflags.io/:country_code/:style/:size.png">

    <img src="https://www.countryflags.io/be/flat/64.png"> -->


    <script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.17/vue.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reconnecting-websocket@4.1.10/dist/reconnecting-websocket-cjs.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue-websocket@0.2.3/dist/vue-websocket.min.js"></script>

    
    <script >
        const app = new Vue({
            el: "#apps",
            data: {
                selected:'A',
                paysA: 'CI',
                pays: [

                    {
                        "name": "Cote D\"Ivoire",
                        "code": "CI"
                    },

                    {
                        "name": "Afghanistan",
                        "code": "AF"
                    },
                    {
                        "name": "Åland Islands",
                        "code": "AX"
                    },
                    {
                        "name": "Albania",
                        "code": "AL"
                    },
                    {
                        "name": "Algeria",
                        "code": "DZ"
                    },
                    {
                        "name": "American Samoa",
                        "code": "AS"
                    },
                    {
                        "name": "AndorrA",
                        "code": "AD"
                    },
                    {
                        "name": "Angola",
                        "code": "AO"
                    },
                    {
                        "name": "Anguilla",
                        "code": "AI"
                    },
                    {
                        "name": "Antarctica",
                        "code": "AQ"
                    },
                    {
                        "name": "Antigua and Barbuda",
                        "code": "AG"
                    },
                    {
                        "name": "Argentina",
                        "code": "AR"
                    },
                    {
                        "name": "Armenia",
                        "code": "AM"
                    },
                    {
                        "name": "Aruba",
                        "code": "AW"
                    },
                    {
                        "name": "Australia",
                        "code": "AU"
                    },
                    {
                        "name": "Austria",
                        "code": "AT"
                    },
                    {
                        "name": "Azerbaijan",
                        "code": "AZ"
                    },
                    {
                        "name": "Bahamas",
                        "code": "BS"
                    },
                    {
                        "name": "Bahrain",
                        "code": "BH"
                    },
                    {
                        "name": "Bangladesh",
                        "code": "BD"
                    },
                    {
                        "name": "Barbados",
                        "code": "BB"
                    },
                    {
                        "name": "Belarus",
                        "code": "BY"
                    },
                    {
                        "name": "Belgium",
                        "code": "BE"
                    },
                    {
                        "name": "Belize",
                        "code": "BZ"
                    },
                    {
                        "name": "Benin",
                        "code": "BJ"
                    },
                    {
                        "name": "Bermuda",
                        "code": "BM"
                    },
                    {
                        "name": "Bhutan",
                        "code": "BT"
                    },
                    {
                        "name": "Bolivia",
                        "code": "BO"
                    },
                    {
                        "name": "Bosnia and Herzegovina",
                        "code": "BA"
                    },
                    {
                        "name": "Botswana",
                        "code": "BW"
                    },
                    {
                        "name": "Bouvet Island",
                        "code": "BV"
                    },
                    {
                        "name": "Brazil",
                        "code": "BR"
                    },
                    {
                        "name": "British Indian Ocean Territory",
                        "code": "IO"
                    },
                    {
                        "name": "Brunei Darussalam",
                        "code": "BN"
                    },
                    {
                        "name": "Bulgaria",
                        "code": "BG"
                    },
                    {
                        "name": "Burkina Faso",
                        "code": "BF"
                    },
                    {
                        "name": "Burundi",
                        "code": "BI"
                    },
                    {
                        "name": "Cambodia",
                        "code": "KH"
                    },
                    {
                        "name": "Cameroon",
                        "code": "CM"
                    },
                    {
                        "name": "Canada",
                        "code": "CA"
                    },
                    {
                        "name": "Cape Verde",
                        "code": "CV"
                    },
                    {
                        "name": "Cayman Islands",
                        "code": "KY"
                    },
                    {
                        "name": "Central African Republic",
                        "code": "CF"
                    },
                    {
                        "name": "Chad",
                        "code": "TD"
                    },
                    {
                        "name": "Chile",
                        "code": "CL"
                    },
                    {
                        "name": "China",
                        "code": "CN"
                    },
                    {
                        "name": "Christmas Island",
                        "code": "CX"
                    },
                    {
                        "name": "Cocos (Keeling) Islands",
                        "code": "CC"
                    },
                    {
                        "name": "Colombia",
                        "code": "CO"
                    },
                    {
                        "name": "Comoros",
                        "code": "KM"
                    },
                    {
                        "name": "Congo",
                        "code": "CG"
                    },
                    {
                        "name": "Congo, The Democratic Republic of the",
                        "code": "CD"
                    },
                    {
                        "name": "Cook Islands",
                        "code": "CK"
                    },
                    {
                        "name": "Costa Rica",
                        "code": "CR"
                    },
                    {
                        "name": "Croatia",
                        "code": "HR"
                    },
                    {
                        "name": "Cuba",
                        "code": "CU"
                    },
                    {
                        "name": "Cyprus",
                        "code": "CY"
                    },
                    {
                        "name": "Czech Republic",
                        "code": "CZ"
                    },
                    {
                        "name": "Denmark",
                        "code": "DK"
                    },
                    {
                        "name": "Djibouti",
                        "code": "DJ"
                    },
                    {
                        "name": "Dominica",
                        "code": "DM"
                    },
                    {
                        "name": "Dominican Republic",
                        "code": "DO"
                    },
                    {
                        "name": "Ecuador",
                        "code": "EC"
                    },
                    {
                        "name": "Egypt",
                        "code": "EG"
                    },
                    {
                        "name": "El Salvador",
                        "code": "SV"
                    },
                    {
                        "name": "Equatorial Guinea",
                        "code": "GQ"
                    },
                    {
                        "name": "Eritrea",
                        "code": "ER"
                    },
                    {
                        "name": "Estonia",
                        "code": "EE"
                    },
                    {
                        "name": "Ethiopia",
                        "code": "ET"
                    },
                    {
                        "name": "Falkland Islands (Malvinas)",
                        "code": "FK"
                    },
                    {
                        "name": "Faroe Islands",
                        "code": "FO"
                    },
                    {
                        "name": "Fiji",
                        "code": "FJ"
                    },
                    {
                        "name": "Finland",
                        "code": "FI"
                    },
                    {
                        "name": "France",
                        "code": "FR"
                    },
                    {
                        "name": "French Guiana",
                        "code": "GF"
                    },
                    {
                        "name": "French Polynesia",
                        "code": "PF"
                    },
                    {
                        "name": "French Southern Territories",
                        "code": "TF"
                    },
                    {
                        "name": "Gabon",
                        "code": "GA"
                    },
                    {
                        "name": "Gambia",
                        "code": "GM"
                    },
                    {
                        "name": "Georgia",
                        "code": "GE"
                    },
                    {
                        "name": "Germany",
                        "code": "DE"
                    },
                    {
                        "name": "Ghana",
                        "code": "GH"
                    },
                    {
                        "name": "Gibraltar",
                        "code": "GI"
                    },
                    {
                        "name": "Greece",
                        "code": "GR"
                    },
                    {
                        "name": "Greenland",
                        "code": "GL"
                    },
                    {
                        "name": "Grenada",
                        "code": "GD"
                    },
                    {
                        "name": "Guadeloupe",
                        "code": "GP"
                    },
                    {
                        "name": "Guam",
                        "code": "GU"
                    },
                    {
                        "name": "Guatemala",
                        "code": "GT"
                    },
                    {
                        "name": "Guernsey",
                        "code": "GG"
                    },
                    {
                        "name": "Guinea",
                        "code": "GN"
                    },
                    {
                        "name": "Guinea-Bissau",
                        "code": "GW"
                    },
                    {
                        "name": "Guyana",
                        "code": "GY"
                    },
                    {
                        "name": "Haiti",
                        "code": "HT"
                    },
                    {
                        "name": "Heard Island and Mcdonald Islands",
                        "code": "HM"
                    },
                    {
                        "name": "Holy See (Vatican City State)",
                        "code": "VA"
                    },
                    {
                        "name": "Honduras",
                        "code": "HN"
                    },
                    {
                        "name": "Hong Kong",
                        "code": "HK"
                    },
                    {
                        "name": "Hungary",
                        "code": "HU"
                    },
                    {
                        "name": "Iceland",
                        "code": "IS"
                    },
                    {
                        "name": "India",
                        "code": "IN"
                    },
                    {
                        "name": "Indonesia",
                        "code": "ID"
                    },
                    {
                        "name": "Iran, Islamic Republic Of",
                        "code": "IR"
                    },
                    {
                        "name": "Iraq",
                        "code": "IQ"
                    },
                    {
                        "name": "Ireland",
                        "code": "IE"
                    },
                    {
                        "name": "Isle of Man",
                        "code": "IM"
                    },
                    {
                        "name": "Israel",
                        "code": "IL"
                    },
                    {
                        "name": "Italy",
                        "code": "IT"
                    },
                    {
                        "name": "Jamaica",
                        "code": "JM"
                    },
                    {
                        "name": "Japan",
                        "code": "JP"
                    },
                    {
                        "name": "Jersey",
                        "code": "JE"
                    },
                    {
                        "name": "Jordan",
                        "code": "JO"
                    },
                    {
                        "name": "Kazakhstan",
                        "code": "KZ"
                    },
                    {
                        "name": "Kenya",
                        "code": "KE"
                    },
                    {
                        "name": "Kiribati",
                        "code": "KI"
                    },
                    {
                        "name": "Korea, Democratic People\"S Republic of",
                        "code": "KP"
                    },
                    {
                        "name": "Korea, Republic of",
                        "code": "KR"
                    },
                    {
                        "name": "Kuwait",
                        "code": "KW"
                    },
                    {
                        "name": "Kyrgyzstan",
                        "code": "KG"
                    },
                    {
                        "name": "Lao People\"S Democratic Republic",
                        "code": "LA"
                    },
                    {
                        "name": "Latvia",
                        "code": "LV"
                    },
                    {
                        "name": "Lebanon",
                        "code": "LB"
                    },
                    {
                        "name": "Lesotho",
                        "code": "LS"
                    },
                    {
                        "name": "Liberia",
                        "code": "LR"
                    },
                    {
                        "name": "Libyan Arab Jamahiriya",
                        "code": "LY"
                    },
                    {
                        "name": "Liechtenstein",
                        "code": "LI"
                    },
                    {
                        "name": "Lithuania",
                        "code": "LT"
                    },
                    {
                        "name": "Luxembourg",
                        "code": "LU"
                    },
                    {
                        "name": "Macao",
                        "code": "MO"
                    },
                    {
                        "name": "Macedonia, The Former Yugoslav Republic of",
                        "code": "MK"
                    },
                    {
                        "name": "Madagascar",
                        "code": "MG"
                    },
                    {
                        "name": "Malawi",
                        "code": "MW"
                    },
                    {
                        "name": "Malaysia",
                        "code": "MY"
                    },
                    {
                        "name": "Maldives",
                        "code": "MV"
                    },
                    {
                        "name": "Mali",
                        "code": "ML"
                    },
                    {
                        "name": "Malta",
                        "code": "MT"
                    },
                    {
                        "name": "Marshall Islands",
                        "code": "MH"
                    },
                    {
                        "name": "Martinique",
                        "code": "MQ"
                    },
                    {
                        "name": "Mauritania",
                        "code": "MR"
                    },
                    {
                        "name": "Mauritius",
                        "code": "MU"
                    },
                    {
                        "name": "Mayotte",
                        "code": "YT"
                    },
                    {
                        "name": "Mexico",
                        "code": "MX"
                    },
                    {
                        "name": "Micronesia, Federated States of",
                        "code": "FM"
                    },
                    {
                        "name": "Moldova, Republic of",
                        "code": "MD"
                    },
                    {
                        "name": "Monaco",
                        "code": "MC"
                    },
                    {
                        "name": "Mongolia",
                        "code": "MN"
                    },
                    {
                        "name": "Montserrat",
                        "code": "MS"
                    },
                    {
                        "name": "Morocco",
                        "code": "MA"
                    },
                    {
                        "name": "Mozambique",
                        "code": "MZ"
                    },
                    {
                        "name": "Myanmar",
                        "code": "MM"
                    },
                    {
                        "name": "Namibia",
                        "code": "NA"
                    },
                    {
                        "name": "Nauru",
                        "code": "NR"
                    },
                    {
                        "name": "Nepal",
                        "code": "NP"
                    },
                    {
                        "name": "Netherlands",
                        "code": "NL"
                    },
                    {
                        "name": "Netherlands Antilles",
                        "code": "AN"
                    },
                    {
                        "name": "New Caledonia",
                        "code": "NC"
                    },
                    {
                        "name": "New Zealand",
                        "code": "NZ"
                    },
                    {
                        "name": "Nicaragua",
                        "code": "NI"
                    },
                    {
                        "name": "Niger",
                        "code": "NE"
                    },
                    {
                        "name": "Nigeria",
                        "code": "NG"
                    },
                    {
                        "name": "Niue",
                        "code": "NU"
                    },
                    {
                        "name": "Norfolk Island",
                        "code": "NF"
                    },
                    {
                        "name": "Northern Mariana Islands",
                        "code": "MP"
                    },
                    {
                        "name": "Norway",
                        "code": "NO"
                    },
                    {
                        "name": "Oman",
                        "code": "OM"
                    },
                    {
                        "name": "Pakistan",
                        "code": "PK"
                    },
                    {
                        "name": "Palau",
                        "code": "PW"
                    },
                    {
                        "name": "Palestinian Territory, Occupied",
                        "code": "PS"
                    },
                    {
                        "name": "Panama",
                        "code": "PA"
                    },
                    {
                        "name": "Papua New Guinea",
                        "code": "PG"
                    },
                    {
                        "name": "Paraguay",
                        "code": "PY"
                    },
                    {
                        "name": "Peru",
                        "code": "PE"
                    },
                    {
                        "name": "Philippines",
                        "code": "PH"
                    },
                    {
                        "name": "Pitcairn",
                        "code": "PN"
                    },
                    {
                        "name": "Poland",
                        "code": "PL"
                    },
                    {
                        "name": "Portugal",
                        "code": "PT"
                    },
                    {
                        "name": "Puerto Rico",
                        "code": "PR"
                    },
                    {
                        "name": "Qatar",
                        "code": "QA"
                    },
                    {
                        "name": "Reunion",
                        "code": "RE"
                    },
                    {
                        "name": "Romania",
                        "code": "RO"
                    },
                    {
                        "name": "Russian Federation",
                        "code": "RU"
                    },
                    {
                        "name": "RWANDA",
                        "code": "RW"
                    },
                    {
                        "name": "Saint Helena",
                        "code": "SH"
                    },
                    {
                        "name": "Saint Kitts and Nevis",
                        "code": "KN"
                    },
                    {
                        "name": "Saint Lucia",
                        "code": "LC"
                    },
                    {
                        "name": "Saint Pierre and Miquelon",
                        "code": "PM"
                    },
                    {
                        "name": "Saint Vincent and the Grenadines",
                        "code": "VC"
                    },
                    {
                        "name": "Samoa",
                        "code": "WS"
                    },
                    {
                        "name": "San Marino",
                        "code": "SM"
                    },
                    {
                        "name": "Sao Tome and Principe",
                        "code": "ST"
                    },
                    {
                        "name": "Saudi Arabia",
                        "code": "SA"
                    },
                    {
                        "name": "Senegal",
                        "code": "SN"
                    },
                    {
                        "name": "Serbia and Montenegro",
                        "code": "CS"
                    },
                    {
                        "name": "Seychelles",
                        "code": "SC"
                    },
                    {
                        "name": "Sierra Leone",
                        "code": "SL"
                    },
                    {
                        "name": "Singapore",
                        "code": "SG"
                    },
                    {
                        "name": "Slovakia",
                        "code": "SK"
                    },
                    {
                        "name": "Slovenia",
                        "code": "SI"
                    },
                    {
                        "name": "Solomon Islands",
                        "code": "SB"
                    },
                    {
                        "name": "Somalia",
                        "code": "SO"
                    },
                    {
                        "name": "South Africa",
                        "code": "ZA"
                    },
                    {
                        "name": "South Georgia and the South Sandwich Islands",
                        "code": "GS"
                    },
                    {
                        "name": "Spain",
                        "code": "ES"
                    },
                    {
                        "name": "Sri Lanka",
                        "code": "LK"
                    },
                    {
                        "name": "Sudan",
                        "code": "SD"
                    },
                    {
                        "name": "Suriname",
                        "code": "SR"
                    },
                    {
                        "name": "Svalbard and Jan Mayen",
                        "code": "SJ"
                    },
                    {
                        "name": "Swaziland",
                        "code": "SZ"
                    },
                    {
                        "name": "Sweden",
                        "code": "SE"
                    },
                    {
                        "name": "Switzerland",
                        "code": "CH"
                    },
                    {
                        "name": "Syrian Arab Republic",
                        "code": "SY"
                    },
                    {
                        "name": "Taiwan, Province of China",
                        "code": "TW"
                    },
                    {
                        "name": "Tajikistan",
                        "code": "TJ"
                    },
                    {
                        "name": "Tanzania, United Republic of",
                        "code": "TZ"
                    },
                    {
                        "name": "Thailand",
                        "code": "TH"
                    },
                    {
                        "name": "Timor-Leste",
                        "code": "TL"
                    },
                    {
                        "name": "Togo",
                        "code": "TG"
                    },
                    {
                        "name": "Tokelau",
                        "code": "TK"
                    },
                    {
                        "name": "Tonga",
                        "code": "TO"
                    },
                    {
                        "name": "Trinidad and Tobago",
                        "code": "TT"
                    },
                    {
                        "name": "Tunisia",
                        "code": "TN"
                    },
                    {
                        "name": "Turkey",
                        "code": "TR"
                    },
                    {
                        "name": "Turkmenistan",
                        "code": "TM"
                    },
                    {
                        "name": "Turks and Caicos Islands",
                        "code": "TC"
                    },
                    {
                        "name": "Tuvalu",
                        "code": "TV"
                    },
                    {
                        "name": "Uganda",
                        "code": "UG"
                    },
                    {
                        "name": "Ukraine",
                        "code": "UA"
                    },
                    {
                        "name": "United Arab Emirates",
                        "code": "AE"
                    },
                    {
                        "name": "United Kingdom",
                        "code": "GB"
                    },
                    {
                        "name": "United States",
                        "code": "US"
                    },
                    {
                        "name": "United States Minor Outlying Islands",
                        "code": "UM"
                    },
                    {
                        "name": "Uruguay",
                        "code": "UY"
                    },
                    {
                        "name": "Uzbekistan",
                        "code": "UZ"
                    },
                    {
                        "name": "Vanuatu",
                        "code": "VU"
                    },
                    {
                        "name": "Venezuela",
                        "code": "VE"
                    },
                    {
                        "name": "Viet Nam",
                        "code": "VN"
                    },
                    {
                        "name": "Virgin Islands, British",
                        "code": "VG"
                    },
                    {
                        "name": "Virgin Islands, U.S.",
                        "code": "VI"
                    },
                    {
                        "name": "Wallis and Futuna",
                        "code": "WF"
                    },
                    {
                        "name": "Western Sahara",
                        "code": "EH"
                    },
                    {
                        "name": "Yemen",
                        "code": "YE"
                    },
                    {
                        "name": "Zambia",
                        "code": "ZM"
                    },
                    {
                        "name": "Zimbabwe",
                        "code": "ZW"
                    }
                ],
                options: [
                    { text: 'Un', value: 'A' },
                    { text: 'Deux', value: 'B' },
                    { text: 'Trois', value: 'C' }
                ]

                
            },
            delimiters: ["${", "}"],
            mounted: function() {
                
            },
            method: {

                choix: function(cd){
                    console.log(cd);
                }

            }
        })
    </script>

   
</body>
</html>


# selet22

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Selct 2</h1>
    <div class="container">
        <div class="header clearfix">
          <h3 class="text-muted">
            Select2 Cascade Demo
            <small>For <a href="http://ajaxray.com/blog/select2-dependent-cascading-select-list-reload/" target="_blank">this post</a></small>
          </h3>
        </div>
  
        <div class="row">
          <div class="col-sm-12">
            
            <form class="form-horizontal">
              <div class="form-group">
                <label for="type" class="col-sm-5 control-label">I'd like to ride</label>   
                <div class="col-sm-5">
                  <select name="type" id="type" class="form-control">
                    <option>--Select your ride--</option>
                    <option value="animals">Animal</option>
                    <option value="vehicles">Vehicle</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label for="subtype" class="col-sm-5 control-label">More specifically</label>       
                <div class="col-sm-5">
                  <select name="subtype" id="subtype"  class="form-control">
                      <option>-- Select type first--</option>
                  </select>
                </div>
              </div>         
            </form>        
        
          </div>
        </div>
  
      </div> <!-- /container -->

        <script src="script.js"></script>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"  crossorigin="anonymous"></script>
        <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css" rel="stylesheet" />
        <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js"></script>
        
        
<script>

    var Select2Cascade = ( function(window, $) {

        function Select2Cascade(parent, child, url, select2Options) {
            var afterActions = [];
            var options = select2Options || {};

            // Register functions to be called after cascading data loading done
            this.then = function(callback) {
                afterActions.push(callback);
                return this;
            };

            parent.select2(select2Options).on("change", function (e) {

                child.prop("disabled", true);

                var _this = this;
                $.getJSON(
                    url.replace(':parentId:', $(this).val()), 
                    console.log($(this).val()),
                    function(items) {
                        var newOptions = '<option value="">-- Select --</option>';
                        for(var id in items) {
                            newOptions += '<option value="'+ id +'">'+ items[id] +'</option>';
                        }

                        child.select2('destroy').html(newOptions).prop("disabled", false)
                            .select2(options);
                        
                        afterActions.forEach(function (callback) {
                            callback(parent, child, items);
                        });
                    });
            });
        }

        return Select2Cascade;

    })( window, $);

    $(document).ready(function() {
        var select2Options = { width: 'resolve' };
        // Loading raw JSON files of a secret gist - https://gist.github.com/ajaxray/32c5a57fafc3f6bc4c430153d66a55f5
        var apiUrl =  'https://gist.githubusercontent.com/ajaxray/32c5a57fafc3f6bc4c430153d66a55f5/raw/260a653e6347fb6d2360e8ec376a2dc4888c1afa/:parentId:.json'; 
        //var apiUrl = 'animals.json'

        $('select').select2(select2Options);                 
        var cascadLoading = new Select2Cascade($('#type'), $('#subtype'), apiUrl, select2Options);
        cascadLoading.then( function(parent, child, items) {
            // Dump response data
            console.log(items);
        });
    });


</script>
    
</body>
</html>


## csss select22
/* Space out content a bit */
body {
    padding-top: 20px;
    padding-bottom: 20px;
  }
  
  /* Everything but the jumbotron gets side spacing for mobile first views */
  .header,
  .marketing,
  .footer {
    padding-right: 15px;
    padding-left: 15px;
  }
  
  /* Custom page header */
  .header {
    padding-bottom: 20px;
    border-bottom: 1px solid #e5e5e5;
  }
  /* Make the masthead heading the same height as the navigation */
  .header h3 {
    margin-top: 0;
    margin-bottom: 0;
    line-height: 40px;
  }
  
  /* Custom page footer */
  .footer {
    padding-top: 19px;
    color: #777;
    border-top: 1px solid #e5e5e5;
  }
  
  /* Customize container */
  @media (min-width: 768px) {
    .container {
      max-width: 730px;
    }
  }
  .container-narrow > hr {
    margin: 30px 0;
  }
  
  /* Supporting marketing content */
  .marketing {
    margin: 40px 0;
  }
  .marketing p + h4 {
    margin-top: 28px;
  }
  
  /* Responsive: Portrait tablets and up */
  @media screen and (min-width: 768px) {
    /* Remove the padding we set earlier */
    .header,
    .marketing,
    .footer {
      padding-right: 0;
      padding-left: 0;
    }
    /* Space out the masthead */
    .header {
      margin-bottom: 30px;
    }
    /* Remove the bottom border on the jumbotron for visual effect */
    .jumbotron {
      border-bottom: 0;
    }
  }
