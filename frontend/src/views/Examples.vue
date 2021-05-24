<template>
  <div class="ma-4">
    <!-- examples of buttons -->
    <p class="title">Buttons</p>
    <v-container>
      <v-btn color="pink lighten-1 white--text" class="mx-2">normal</v-btn>
      <v-btn depressed color="pink lighten-1 white--text" class="mx-2"
        >depressed</v-btn
      >
      <v-btn plain color="pink lighten-1 white--text" class="mx-2">plain</v-btn>
      <v-btn color="pink lighten-1 white--text" class="mx-2"
        ><v-icon left>mdi-email</v-icon>icon</v-btn
      >
      <v-btn small color="pink lighten-1 white--text" class="mx-2">small</v-btn>
      <v-btn large color="pink lighten-1 white--text" class="mx-2">large</v-btn>
      <v-btn fab color="pink lighten-1" class="mx-2" dark
        ><v-icon>mdi-heart</v-icon></v-btn
      >
      <v-btn color="pink lighten-1 white--text" class="mx-2" outlined
        >outlined</v-btn
      >
      <v-btn
        color="pink lighten-1 white--text"
        class="mx-2"
        @click="snackBar = true"
        >Open snackbar</v-btn
      >
      <v-snackbar v-model="snackBar">
        {{ text }}

        <template v-slot:action="{ attrs }">
          <v-btn color="pink" text v-bind="attrs" @click="snackBar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
      <v-btn block color="pink lighten-1 white--text my-4 ml-2">block</v-btn>
    </v-container>
    <!-- Text layout -->
    <p class="title">Text layout</p>
    <v-container class="my-5">
      <v-row>
        <v-col cols="12" sm="6">
          <div class="caption grey--text">Project Title</div>
          <div>Create a new website</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Person</div>
          <div>Anzelika</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Due Date</div>
          <div>02/04/20</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Status</div>
          <div>ongoing</div>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
    <v-container class="my-5">
      <v-row>
        <v-col cols="6" sm="3">
          <div class="caption grey--text">Name</div>
          <div>Loulou</div>
        </v-col>
        <v-col cols="6" sm="3">
          <div class="caption grey--text">Age</div>
          <div>20</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Birth</div>
          <div>2021/6/4</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Sexual</div>
          <div>male</div>
        </v-col>
        <v-col sm="2">
          <div class="caption grey--text">Rating</div>
          <div>99</div>
        </v-col>
      </v-row>
    </v-container>
    <!-- text fields -->
    <p class="title">Text fields</p>

    <v-container>
      <v-row>
        <v-col cols="6" sm="4">
          <v-text-field label="regular style"></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="solo style" solo></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="filled style" filled></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="outlined style" outlined></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="rounded style" rounded filled></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="color"
            color="purple"
            value="click me!"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="disabled" disabled></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="readonly"
            readonly
            placeholder="input not allowed"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="place holder"
            placeholder="place holder here"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="hint" hint="hint here"></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="clearable"
            clearable
            value="clearable"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            value="15 words limit"
            label="counter"
            counter="15"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            :rules="[rules.counter15]"
            value="15 words exceeded"
            label="counter"
            counter="15"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            :rules="[rules.required]"
            label="hide details"
            hide-details="auto"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="mdi-map-marker"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="Prepend"
            prepend-icon="mdi-map-marker"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="Append"
            append-icon="mdi-map-marker"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            label="Append outer"
            append-outer-icon="mdi-map-marker"
          ></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="prefix" value="298" prefix="￥"></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field label="suffix" value="180" suffix="cm"></v-text-field>
        </v-col>
        <v-col cols="6" sm="4">
          <v-text-field
            value="12345"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required]"
            :type="show ? 'text' : 'password'"
            label="password"
            counter
            @click:append="show = !show"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
    <!-- radio buttons -->
    <p class="title">Radio buttons</p>
    <v-container>
      <v-row>
        <v-col cols="3"
          ><v-radio-group v-model="radioGroup">
            <v-radio
              v-for="n in 3"
              :key="n"
              :label="`Radio ${n}`"
              :value="n"
            ></v-radio>

            <p>radio value: {{ radioGroup }}</p>
          </v-radio-group>
        </v-col>
        <v-col cols="3"
          ><v-radio-group>
            <v-radio label="primary" color="primary" value="primary"></v-radio>
            <v-radio
              label="secondary"
              color="secondary"
              value="secondary"
            ></v-radio>
            <v-radio label="success" color="success" value="success"></v-radio>
            <v-radio label="info" color="info" value="info"></v-radio>
            <v-radio label="warning" color="warning" value="warning"></v-radio>
            <v-radio
              label="error"
              color="error"
              value="error"
            ></v-radio> </v-radio-group
        ></v-col>
        <v-col cols="3">
          <v-radio-group column>
            <v-radio label="column 1" value="radio-1"></v-radio>
            <v-radio label="column 2" value="radio-2"></v-radio>
          </v-radio-group>
        </v-col>
        <v-col cols="3">
          <v-radio-group row>
            <v-radio label="row 1" value="radio-1"></v-radio>
            <v-radio label="row 2" value="radio-2"></v-radio>
          </v-radio-group>
        </v-col>
      </v-row>
    </v-container>
    <!-- check boxes -->
    <p class="title">Check boxes</p>
    <v-container>
      <v-row>
        <v-col cols="3">
          <v-container class="px-0" fluid>
            <v-checkbox
              v-model="checkBox"
              :label="`Checkbox : ${checkBox.toString()}`"
            ></v-checkbox>
          </v-container>
        </v-col>
        <v-col col="4">
          <v-checkbox
            v-for="n in 3"
            :key="n"
            :label="'red ' + n"
            :color="'red lighten-' + n"
            input-value="true"
          ></v-checkbox>
        </v-col>
        <v-col col="3">
          <v-checkbox
            v-for="n in 3"
            :key="n"
            :label="'blue ' + n"
            :color="'blue lighten-' + n"
            input-value="true"
          ></v-checkbox>
        </v-col>
        <v-col col="3">
          <v-checkbox
            v-for="n in 3"
            :key="n"
            :label="'green ' + n"
            :color="'green lighten-' + n"
            input-value="true"
          ></v-checkbox>
        </v-col>
      </v-row>
    </v-container>
    <!-- selector -->
    <p class="title">Selector</p>
    <v-container>
      <v-row>
        <v-col cols="3">
          <v-select :items="selectItems" label="normal style"> </v-select>
        </v-col>
        <v-col cols="3">
          <v-select :items="selectItems" label="filled style" filled>
          </v-select>
        </v-col>
        <v-col cols="3">
          <v-select :items="selectItems" label="outlined style" outlined>
          </v-select>
        </v-col>
        <v-col cols="3">
          <v-select :items="selectItems" label="solo sytle" solo> </v-select>
        </v-col>
        <v-col cols="3">
          <v-select v-model="e1" :items="selectItems" label="multiple" multiple>
          </v-select>
        </v-col>
        <v-col cols="3">
          <v-select
            v-model="e1"
            :items="selectItems"
            label="multiple chips"
            chips
            multiple
          >
          </v-select>
        </v-col>
      </v-row>
    </v-container>
    <!-- selector -->
    <p class="title">Switches</p>
    <v-container>
      <v-row>
        <v-col cols="4">
          <v-switch
            v-for="n in 3"
            :key="n"
            :color="`purple lighten-${n}`"
            :label="`purple ${n}`"
            input-value="true"
          ></v-switch
        ></v-col>
        <v-col cols="4">
          <v-switch
            v-for="n in 3"
            :key="n"
            :color="`brown lighten-${n}`"
            :label="`brown ${n}`"
            input-value="true"
          ></v-switch>
        </v-col>
        <v-col cols="4">
          <v-switch
            v-for="n in 3"
            :key="n"
            :color="`orange lighten-${n}`"
            :label="`orange ${n}`"
            input-value="true"
          ></v-switch>
        </v-col>
        <v-col cols="4">
          <v-switch v-model="show" :label="`Switch : ${show.toString()}`">
          </v-switch>
          <v-switch v-model="show" label="flat" flat> </v-switch>
          <v-switch v-model="show" label="inset" inset> </v-switch>
        </v-col>
        <v-col cols="4">
          <v-switch v-model="heroes" label="Genji" value="Genji"></v-switch>
          <v-switch v-model="heroes" label="Tracer" value="Tracer"></v-switch>
          <v-switch v-model="heroes" label="Mercy" value="Mercy"></v-switch>
          <p>{{ heroes }}</p>
        </v-col>
        <v-col cols="4">
          <v-switch label="on disabled" disabled input-value="1"></v-switch>
          <v-switch label="off disabled" disabled></v-switch>
          <v-switch label="loading" loading></v-switch>
        </v-col>
      </v-row>
    </v-container>
    <!-- slider -->
    <p class="title">Sliders</p>
    <v-container>
      <v-row>
        <v-col cols="6">
          <v-slider
            hint="Im a hint"
            max="50"
            min="-50"
            label="normal"
            value="15"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            thumb-color="red"
            label="red thumb"
            value="15"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            track-color="green"
            label="green track"
            value="15"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            track-color="green"
            label="thumb label"
            value="-5"
            thumb-label="always"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            label="disabled"
            value="-10"
            disabled
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            label="ticks"
            value="7"
            ticks="always"
            step="10"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="50"
            min="-50"
            label="inversed label"
            inverse-label
            value="4"
          ></v-slider>
        </v-col>
        <v-col cols="6">
          <v-slider
            max="4"
            label="tick values"
            :tick-labels="selectItems"
            step="1"
            value="2"
          ></v-slider>
        </v-col>
      </v-row>
    </v-container>
    <!-- file input -->
    <p class="title">File inputs</p>
    <v-container>
      <v-file-input
        chips
        show-size
        counter
        placeholder="Pick an avatar"
        :rules="[rules.fileSize]"
      >
      </v-file-input>
    </v-container>
    <!-- text areas -->
    <p class="title">Text areas</p>
    <v-container>
      <v-row>
        <v-col cols="6">
          <v-textarea
            label="default style"
            hint="Hint text"
            value="
            Why are you worrying about YOU-KNOW-WHO?
            You should be worrying about U-NO-POO!"
          ></v-textarea>
        </v-col>
        <v-col cols="6">
          <v-textarea
            label="outlined style"
            outlined
            value="
            Why are you worrying about YOU-KNOW-WHO?
            You should be worrying about U-NO-POO!"
          ></v-textarea>
        </v-col>
        <v-col cols="6">
          <v-textarea
            label="solo style"
            solo
            value="
            Why are you worrying about YOU-KNOW-WHO?
            You should be worrying about U-NO-POO!"
          ></v-textarea>
        </v-col>
        <v-col cols="6">
          <v-textarea
            label="filled style"
            filled
            value="
            Why are you worrying about YOU-KNOW-WHO?
            You should be worrying about U-NO-POO!"
          ></v-textarea>
        </v-col>
      </v-row>
    </v-container>
    <!-- paginations -->
    <p class="title">Paginations</p>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6">
          <v-pagination v-model="page" :length="5"></v-pagination
        ></v-col>
        <v-col cols="12" sm="6">
          <v-pagination v-model="page" :length="5" circle></v-pagination
        ></v-col>
      </v-row>
    </v-container>
    <!-- selectors -->
    <p class="title">Selectors</p>
    <v-container>
      <v-row justify="left">
        <v-col
          ><v-date-picker v-model="datePicker" scrollable></v-date-picker
        ></v-col>
        <v-col
          ><v-date-picker
            v-model="datePicker"
            type="month"
            color="red"
          ></v-date-picker
        ></v-col>
        <v-col
          ><v-date-picker
            v-model="datePicker"
            multiple
            color="green"
          ></v-date-picker
        ></v-col>
        <v-col><v-time-picker scrollable></v-time-picker></v-col>
        <v-col><v-time-picker color="red"></v-time-picker></v-col>
        <v-col
          ><v-time-picker color="green" format="24hr"></v-time-picker
        ></v-col>
      </v-row>
    </v-container>
  </div>
</template> 

<script>
export default {
  data() {
    return {
      snackBar: false,
      text: "Hello~",
      datePicker: new Date().toISOString().substr(0, 10),
      page: 1,
      show: true,
      checkBox: 1,
      radioGroup: 1,
      heroes: ["Genji"],
      e1: ["Lucio", "Genji"],
      selectItems: ["Dva", "Tracer", "Wrecking Ball", "Lucio", "Genji"],
      rules: {
        counter15: (v) => v.length <= 15 || "Max 15 characters",
        required: (v) => !!v || "Required.",
        fileSize: (v) =>
          !v || v.size < 2000000 || "Avatar size should be less than 2 MB!",
      },
    };
  },
};
</script>
