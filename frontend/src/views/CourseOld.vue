<template>
  <v-container fluid>
    <!-- 个人信息 -->
    <v-row>
      <v-col v-for="field in stuInfoCol" :key="field[0]" :cols="field[1]">
        <div class="subtitle-2 grey--text">
          {{ field[0] }}
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <div>{{ stuInfo.stu_id }}</div>
      </v-col>
      <v-col>
        <div>{{ stuInfo.name }}</div>
      </v-col>
      <v-col>
        <div>{{ stuInfo.grade }}</div>
      </v-col>
      <v-col cols="3">
        <div>{{ stuInfo.academy }}</div>
      </v-col>
      <v-col>
        <div>{{ stuInfo.campus }}</div>
      </v-col>
      <v-col>
        <div>{{ stuInfo.credit }}</div>
      </v-col>
    </v-row>
    <!-- 课程排名 -->
    <v-row class="ma-10">
      <v-col>
        <v-card>
          <v-container class="py-7">
            <!-- 字段 -->
            <v-row>
              <v-col
                v-for="field in courseRankCol"
                :key="field[0]"
                :cols="field[1]"
              >
                <div class="subtitle-2 grey--text">{{ field[0] }}</div>
              </v-col>
            </v-row>
            <!-- 具体内容 -->
            <v-row v-for="course in courseRank" :key="course.course_id">
              <v-col>
                <div>{{ course.course_id }}</div>
              </v-col>
              <v-col cols="3">
                <div>{{ course.course_name }}</div> </v-col
              ><v-col>
                <div>{{ course.teacher_id }}</div> </v-col
              ><v-col>
                <div>{{ course.teacher_name }}</div> </v-col
              ><v-col>
                <div>{{ course.capacity }}</div> </v-col
              ><v-col>
                <div>{{ course.number }}</div> </v-col
              ><v-col>
                <div>{{ course.rank }}</div>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
    <!-- 课程信息 -->
    <v-row class="ma-8">
      <v-col>
        <v-card>
          <v-container fluid class="px-7">
            <!-- 字段 -->
            <v-row>
              <v-col
                v-for="field in courseInfoCol"
                :key="field[0]"
                :cols="field[1]"
              >
                <div class="subtitle-2 grey--text">{{ field[0] }}</div>
              </v-col>
            </v-row>
            <!-- 具体内容 -->
            <v-row v-for="course in courseInfo" :key="course.course_id">
              <v-col>
                <div>{{ course.id }}</div>
              </v-col>
              <v-col>
                <div>{{ course.course_id }}</div>
              </v-col>
              <v-col cols="2">
                <div>{{ course.course_name }}</div>
              </v-col>
              <v-col>
                <div>{{ course.credit }}</div>
              </v-col>
              <v-col>
                <div>{{ course.teacher_id }}</div>
              </v-col>
              <v-col>
                <div>{{ course.teacher_name }}</div>
              </v-col>
              <v-col cols="2">
                <div>{{ course.course_time }}</div>
              </v-col>
              <v-col>
                <div>{{ course.course_location }}</div>
              </v-col>
              <v-col>
                <div>{{ course.question_time }}</div>
              </v-col>
              <v-col>
                <div>{{ course.question_location }}</div>
              </v-col>
              <v-col>
                <div>{{ course.campus }}</div>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
    <!-- 课表 -->
    <v-row class="ma-8">
      <v-col>
        <v-card>
          <v-container fluid class="py-5">
            <!-- 字段 -->
            <v-row>
              <v-col
                v-for="field in courseTableCol"
                :key="field[0]"
                :cols="field[1]"
              >
                <div class="subtitle-2 grey--text">{{ field[0] }}</div>
              </v-col>
            </v-row>
            <!-- 具体内容 -->
            <v-row v-for="course in courseTable" :key="course.id">
              <v-col>
                <div>{{ course.id }}</div>
              </v-col>
              <v-col cols="3">
                <div>{{ course.time }}</div>
              </v-col>
              <v-col>
                <div>{{ course.Mon }}</div>
              </v-col>
              <v-col>
                <div>{{ course.Tues }}</div>
              </v-col>
              <v-col>
                <div>{{ course.Wed }}</div>
              </v-col>
              <v-col>
                <div>{{ course.Thur }}</div>
              </v-col>
              <v-col>
                <div>{{ course.Fri }}</div>
              </v-col>
            </v-row>
            <v-row> </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {
  readCourseRankAPI,
  readCourseInfoAPI,
  readCourseTableAPI,
  readStuInfoAPI,
} from "@/api/course";
export default {
  name: "Course",
  data() {
    return {
      stuInfoCol: [
        ["学号"],
        ["姓名"],
        ["年级"],
        ["学院", 3],
        ["校区"],
        ["学分"],
      ],
      stuInfo: [],
      courseRankCol: [
        ["课程号", 1.5],
        ["课程名", 3],
        ["教师号", 1.5],
        ["教师名", 1.5],
        ["容量", 1.5],
        ["选课人数", 1.5],
        ["排名", 1.5],
      ],
      courseRank: [],
      courseInfoCol: [
        ["#"],
        ["课程号"],
        ["课程名", 2],
        ["学分"],
        ["教师号"],
        ["教师名"],
        ["上课时间", 2],
        ["上课地点"],
        ["答疑时间"],
        ["答疑地点"],
        ["校区"],
      ],
      courseInfo: [],
      courseTableCol: [
        ["#"],
        ["时间", 3],
        ["一"],
        ["二"],
        ["三"],
        ["四"],
        ["五"],
      ],
      courseTable: [],
    };
  },
  mounted: function () {
    this.readCourseRank();
    this.readCourseInfo();
    this.readCourseTable();
    this.readStuInfo();
  },
  methods: {
    readCourseRank() {
      readCourseRankAPI().then((res) => {
        this.courseRank = res;
      });
    },
    readCourseInfo() {
      readCourseInfoAPI().then((res) => {
        this.courseInfo = res;
      });
    },
    readCourseTable() {
      readCourseTableAPI().then((res) => {
        this.courseTable = res;
      });
    },
    readStuInfo() {
      readStuInfoAPI().then((res) => {
        this.stuInfo = res;
      });
    },
  },
};
</script>