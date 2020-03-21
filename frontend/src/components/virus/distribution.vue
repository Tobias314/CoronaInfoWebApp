<template>
  <body>
    <h3>
      Wie ist die Ausbreitung?
    </h3>
    <div>
    <md-table>
      <md-table-row>
        <md-table-head>Anzahl Fälle in {{casecount.type}} {{ this.$parent.location }}</md-table-head>
        <md-table-head>Änderungsrate</md-table-head>
        <md-table-head>Zeit</md-table-head>
      </md-table-row>

      <md-table-row>
        <md-table-cell>{{casecount.number_cases}}</md-table-cell>
        <md-table-cell>{{casecount.change_rate}}</md-table-cell>
        <md-table-cell>{{casecount.time}}</md-table-cell>
      </md-table-row>
    </md-table>
    </div>
  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'general_info',

  data:function(){
    return{
      casecount: "",
    }
  },

  mounted(){
    Api.get(`/district_case_number/${this.$parent.location}`)
    .then(response => {
      this.casecount = response.data;
    }, error => {
      console.error(error);
    });
  }
}
</script>

<style>

</style>
