module.exports = function(grunt) {

  // Configurable paths
  var config = {
    src: 'django-project',
    build: 'django-project/build'
  };

  // Project configuration.
  grunt.initConfig({
    config: config,
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.

    concat: {
      app: {
        src: ['<%= config.src %>/static/js/app/**/*.js'],
        dest: '<%= config.build %>/static/js/app.js'
      },
      vendor: {
        src: ['<%= config.src %>/static/js/vendor/**/*.js'],
        dest: '<%= config.build %>/static/js/lib.js'
      }
    },

    uglify: {
      app: {
        files: {
          '<%= config.build %>/static/js/app.min.js': ['<%= config.src %>/static/js/app/**/*.js']
        }
      },
      vendor: {
        files: {
          '<%= config.build %>/static/js/lib.min.js': ['<%= config.src %>/static/js/vendor/**/*.js']
        }
      }
    },

    sass: {
      dev: {
        options: {
          sourceMap: true
        },
        files: {
          '<%= config.build %>/static/css/main.css': '<%= config.src %>/static/scss/main.scss'
        }
      },
      deploy: {
        options: {
          sourceMap: true,
          outputStyle: 'compressed'
        },
        files: {
          '<%= config.build %>/static/css/main.min.css': '<%= config.src %>/static/scss/main.scss'
        }
      }
    },

    bowercopy: {
      options: {
        srcPrefix: ''
      },
      scripts: {
        options: {
          destPrefix: '<%= config.build %>/static/js'
        },
        files: {
          'jquery.min.js': 'bower_components/jquery/dist/jquery.min.js',
          'materialize.min.js': 'bower_components/Materialize/dist/js/materialize.min.js'
        }
      },
      css: {
        options: {
          destPrefix: '<%= config.build %>/static/css'
        },
        files: {
          'materialize.min.css': 'bower_components/Materialize/dist/css/materialize.min.css',
          'materialdesignicons.min.css': 'bower_components/mdi/css/materialdesignicons.min.css'
        }
      },
      fonts: {
        options: {
          destPrefix: '<%= config.build %>/static/fonts'
        },
        files: {
          'materialdesignicons-webfont.eot': 'bower_components/mdi/fonts/materialdesignicons-webfont.eot',
          'materialdesignicons-webfont.svg': 'bower_components/mdi/fonts/materialdesignicons-webfont.svg',
          'materialdesignicons-webfont.ttf': 'bower_components/mdi/fonts/materialdesignicons-webfont.ttf',
          'materialdesignicons-webfont.woff': 'bower_components/mdi/fonts/materialdesignicons-webfont.woff',
          'materialdesignicons-webfont.woff2': 'bower_components/mdi/fonts/materialdesignicons-webfont.woff2'
        }
      },
      font: {
        options: {
          destPrefix: '<%= config.build %>/static/font'
        },
        files: {
          'material-design-icons/Material-Design-Icons.eot': 'bower_components/Materialize/font/material-design-icons/Material-Design-Icons.eot',
          'material-design-icons/Material-Design-Icons.svg': 'bower_components/Materialize/font/material-design-icons/Material-Design-Icons.svg',
          'material-design-icons/Material-Design-Icons.ttf': 'bower_components/Materialize/font/material-design-icons/Material-Design-Icons.ttf',
          'material-design-icons/Material-Design-Icons.woff': 'bower_components/Materialize/font/material-design-icons/Material-Design-Icons.woff',
          'material-design-icons/Material-Design-Icons.woff2': 'bower_components/Materialize/font/material-design-icons/Material-Design-Icons.woff2',
          'roboto/Roboto-Thin.eot': '<%= config.src %>/static/fonts/Roboto-Thin.eot',
          'roboto/Roboto-Thin.ttf': 'bower_components/Materialize/font/roboto/Roboto-Thin.ttf',
          'roboto/Roboto-Thin.woff': 'bower_components/Materialize/font/roboto/Roboto-Thin.woff',
          'roboto/Roboto-Thin.woff2': 'bower_components/Materialize/font/roboto/Roboto-Thin.woff2',
          'roboto/Roboto-Bold.eot': '<%= config.src %>/static/fonts/Roboto-Bold.eot',
          'roboto/Roboto-Bold.ttf': 'bower_components/Materialize/font/roboto/Roboto-Bold.ttf',
          'roboto/Roboto-Bold.woff': 'bower_components/Materialize/font/roboto/Roboto-Bold.woff',
          'roboto/Roboto-Bold.woff2': 'bower_components/Materialize/font/roboto/Roboto-Bold.woff2',
          'roboto/Roboto-Light.eot': '<%= config.src %>/static/fonts/Roboto-Light.eot',
          'roboto/Roboto-Light.ttf': 'bower_components/Materialize/font/roboto/Roboto-Light.ttf',
          'roboto/Roboto-Light.woff': 'bower_components/Materialize/font/roboto/Roboto-Light.woff',
          'roboto/Roboto-Light.woff2': 'bower_components/Materialize/font/roboto/Roboto-Light.woff2',
          'roboto/Roboto-Medium.eot': '<%= config.src %>/static/fonts/Roboto-Medium.eot',
          'roboto/Roboto-Medium.ttf': 'bower_components/Materialize/font/roboto/Roboto-Medium.ttf',
          'roboto/Roboto-Medium.woff': 'bower_components/Materialize/font/roboto/Roboto-Medium.woff',
          'roboto/Roboto-Medium.woff2': 'bower_components/Materialize/font/roboto/Roboto-Medium.woff2',
          'roboto/Roboto-Regular.eot': '<%= config.src %>/static/fonts/Roboto-Regular.eot',
          'roboto/Roboto-Regular.ttf': 'bower_components/Materialize/font/roboto/Roboto-Regular.ttf',
          'roboto/Roboto-Regular.woff': 'bower_components/Materialize/font/roboto/Roboto-Regular.woff',
          'roboto/Roboto-Regular.woff2': 'bower_components/Materialize/font/roboto/Roboto-Regular.woff2',

        }
      }
    },

    imagemin: { // Task
      dynamic: { // Another target
        files: [{
          expand: true, // Enable dynamic expansion
          cwd: '<%= config.src %>/static/images/', // Src matches are relative to this path
          src: ['**/*.{png,jpg,gif}'], // Actual patterns to match
          dest: '<%= config.build %>/static/images/' // Destination path prefix
        }]
      }
    },

    copy: {
      main: {
        expand: true,
        cwd: '<%= config.src %>/static/css/',
        src: 'summernote2.css',
        dest: '<%= config.build %>/static/css/',
      },
    },

    watch: {
      options: {
        livereload: true
      },
      javascript: {
        files: ['<%= config.src %>/static/js/app/**/*.js'],
        tasks: ['concat']
      },
      sass: {
        files: '<%= config.src %>/static/scss/**/*.scss',
        tasks: ['sass:dev']
      }
    }

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-bowercopy');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');

  // Register tasks here.
  grunt.registerTask('default', [
    'concat',
    'uglify',
    'sass',
    'bowercopy',
    'imagemin',
    'copy'
  ]);

  grunt.registerTask('serve', [
    'concat',
    'uglify',
    'sass',
    'bowercopy',
    'imagemin',
    'copy',
    'watch'
  ]);

};
