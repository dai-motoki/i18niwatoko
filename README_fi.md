# Monikielinen käännös i18niwatoko

i18niwatoko on tekoälytyökalu, joka kääntää kaikilta kieliltä kaikille kielille.

## i18niwatokon filosofia

Tavoitteena on maailma, jossa kaikki voivat nauttia ohjelmoinnista kielimuurin yli.

i18niwatoko on innovatiivinen työkalu, joka ratkaisee monikielisen käännöksen haasteet. Perinteisissä monikielisissä käännöstyökaluissa on ollut ongelmana, että ne käsittelevät pääasiassa englanninkielisiä ohjelmointikieliä, mikä on asettanut esteen ei-englanninkielisille käyttäjille.

i18niwatoko on kuitenkin erilainen. Se on luonnollisella kielellä toimiva ohjelmointikieli, jolla kaikki voivat kirjoittaa ohjelmia äidinkielellään. Lisäksi i18niwatokolla on toiminto, joka kääntää automaattisesti japaninkielisiä viestintiedostoja useille kielille. Tämä poistaa manuaalisen käännöstyön tarpeen ja mahdollistaa tehokkaan monikielisen tuen.

Ohjelmointi ei ole vain tiettyjen lahjakkaiden ihmisten etuoikeus. Poistamalla kielimuurin, mahdollistamme sen, että kaikki ihmiset ympäri maailmaa voivat kokea ohjelmoinnin ilon ja mahdollisuudet. Tämä on i18niwatokon jalomielinen päämäärä.

Yhdessä i18niwatokon kanssa kunnioitamme kielellisen moninaisuuden arvoa ja käytämme teknologian voimaa yhdistääksemme ihmisiä. Tavoitteenamme on luoda yhteiskunta, jossa ihmiset voivat toteuttaa luovuuttaan ja synnyttää uusia ideoita ohjelmoinnin kautta.

## Tarvittavat komponentit

- Python 3.x
- niwatoko-kirjasto
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Asennus

1. Asenna niwatoko-kirjasto.

   ```
   pip install --upgrade niwatoko
   ```

2. Määritä OpenAI, Anthropic ja GCP Vertex AI -asetukset.

   ```
   # Aseta OpenAI API-avain
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Aseta Anthropic API-avain
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Määritä GCP Vertex AI
   # Hanki GCP Vertex AI -projektin ID ja sijainti (jos unohdat, ota yhteyttä Motokin X:ään https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Käyttö

1. Valmistele käännösmääritystiedosto (`def_translation.md`).

2. Suorita seuraava komento käännöksen aloittamiseksi. (gemini-1.5-flash on vakaa versio.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Kun käännös on valmis, kunkin kielen viestintiedostot luodaan.

4