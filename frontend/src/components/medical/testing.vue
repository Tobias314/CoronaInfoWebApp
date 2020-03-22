<template>
  <body>
  <span> Befor Sie anrufen, führen Sie zunächst den Coronatest der CovApp durch. Nur wenn dieser eine Testung empfiehlt,
         haben Sie in den meisten Kreisen eine Chance für einen Test. Falls Sie weitere Fragen haben, bieten viele Kreise
         eine Buergerhotline an. An diese können Sie sich wenden. Falls ihnen CovApp eine Testung empfiehlt, wenden Sie sich
        an unten genannte Anlaufstellen, um das weitere Verfahren in ihrem Kreis zu besprechen.
  </span>
    <h3> Buergerhotline </h3>
    <span class="number"> {{ this.citizenhotline }} </span>
    <h3> Kontakt für Test </h3>
    <span class="number"> {{this.testhotline}} </span>
    <h3> Weiteres </h3>
    <span>
        Weitere Informationen über Coronavirus in ihrem Kreis finden sie <a target="_blank" rel="noopener noreferrer" :href="website">hier</a>
    </span>


  </body>
</template>



<script>
  import Api from "../api.js";

  export default {
    name: 'GeneralInfo',
    data() {
      return {
        citizenhotline: " ",
        testhotline: " ",
        website: " "
      };
    },

    created() {
      Api.get(`/district_infos/${this.$parent.location}`)
        .then(response => {
          this.citizenhotline = response.data["citizen_hotline"];
          this.testhotline = response.data["test_hotline"];
          this.website = response.data["info_web_page"];
          console.log(this.website);
        }
      )
    }
  }
</script>

<style>

</style>