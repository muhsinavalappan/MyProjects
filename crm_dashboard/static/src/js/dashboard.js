odoo.define("crm_dashboard.crm_dashboard_action", function(require) {
	"use strict";
	var AbstractAction = require('web.AbstractAction');
	var core = require('web.core');
	var QWeb = core.qweb;
	var session = require('web.session');
	var model = require('web.Model');
	var rpc = require('web.rpc');
	var self = this;
	var DashBoard = AbstractAction.extend({
		contentTemplate: 'DashboardDashboard',
		events: {
			'click .my_lead': 'on_click_my_lead',
			'click .opportunity': 'on_click_opportunity',
			'change #filter_values': function(e) {
				e.stopPropagation();
				var $target = $(e.target);
				var values = $target.val();
				if (values == 'this_year') {
					this.onClick_this_year($target.val());
					this.render_my_leads_graph_year();
					this.render_opportunity_graph_year();
				}
				if (values == 'this_month') {
					this.onClick_this_year($target.val());
					this.render_my_leads_graph_month();
					this.render_opportunity_graph_month();
				}
				if (values == 'this_week') {
					this.onClick_this_year($target.val());
					this.render_my_leads_graph_week();
					this.render_opportunity_graph_week();
				}
				if (values == 'this_quarter') {
					this.onClick_this_year($target.val());
					this.render_my_leads_graph_quarter();
					this.render_opportunity_graph_quarter();
				}
			},
		},
		init: function(parent, context) {
			this._super(parent, context);
			this.dashboards_templates = ['LoginUser', 'MainSection'];
		},
		start: function() {
			var self = this;
			this.set("title", 'Dashboard');
			return this._super().then(function() {
				self.render_dashboards();
				self.render_my_leads_graph();
			});
		},
		willStart: function() {
			var self = this;
			return this._super()
		},
		render_dashboards: function() {
			var self = this;
			this.fetch_data()
			var templates = ['LoginUser', 'MainSection'];
			_.each(templates, function(template) {
				self.$('.o_hr_dashboard').append(QWeb.render(template, {
					widget: self
				}))
			});
		},
		fetch_data: function() {
			var self = this
			var def0 = self._rpc({
				model: 'crm.lead',
				method: 'check_user_group'
			}).then(function(result) {
				if (result == true) {
					self.is_manager = true;
				} else {
					self.is_manager = false;
				}
			});

			var def1 = this._rpc({
					model: 'crm.lead',
					method: "get_data",
				})
				.then(function(result) {
					$('#lead_templates').append('<span>' + result.lead_templates + '</span>');
					$('#opportunity_templates').append('<span>' + result.opportunity_templates + '</span>');
					$('#expected_revenue').append('<span>' + result.currency_id + '</span>');
					$('#expected_revenue').append('<span>' + result.expected_revenue + '</span>');
					$('#revenue').append('<span>' + result.currency_id + '</span>');
					$('#revenue').append('<span>' + result.order_id + '</span>');
					$('#win_ratio').append('<span>' + result.win_ratio + '</span>');
				});
			return $.when(def0, def1);

		},
		on_click_my_lead: function(ev) {
			ev.preventDefault();
			var $action = $(ev.currentTarget);
			var lead_val = this.$('#filter_values').val();
			var self = this;
			var domain = [
				['type', '=', 'lead']
			];
			if (self.is_manager == false) {
				domain.push(['user_id', '=', session.uid]);
			}
			if (lead_val == "this_year") {
				var context = "";
			}
			var today = new Date();
			var quarter = Math.floor((today.getMonth() + 3) / 3);
			if (lead_val == "this_quarter") {
				var context = {
					'search_default_creation_date': quarter
				};
			}

			if (lead_val == "this_month") {
				var context = {
					'search_default_creation_date': today.getMonth() + 1
				};
			}
			var week_start = (new Date(today.setDate(today.getDate() - today.getDay()))).toLocaleDateString();
			var week_end = (new Date(today.setDate(today.getDate() - today.getDay() + 6))).toLocaleDateString();
			if (lead_val == "this_week") {
				domain.push(['create_date', '>=', week_start], ['create_date', '<=', week_end]);
			}
			this.do_action({
				type: 'ir.actions.act_window',
				name: 'Lead',
				res_model: 'crm.lead',
				views: [
					[false, 'tree'],
					[false, 'form']
				],
				domain: domain,
				context: context,
				target: 'current',
			});

		},

		on_click_opportunity: function(ev) {
			ev.preventDefault();
			var $action = $(ev.currentTarget);
			var lead_val = this.$('#filter_values').val();
			var self = this;
			var domain = [
				['type', '=', 'opportunity']
			];
			if (self.is_manager == false) {
				domain.push(['user_id', '=', session.uid]);
			}
			if (lead_val == "this_year") {
				var context = "";
			}
			var today = new Date();
			var quarter = Math.floor((today.getMonth() + 3) / 3);
			if (lead_val == "this_quarter") {
				var context = {
					'search_default_creation_date': quarter
				};
			}

			if (lead_val == "this_month") {
				var context = {
					'search_default_creation_date': today.getMonth() + 1
				};
			}
			var week_start = (new Date(today.setDate(today.getDate() - today.getDay()))).toLocaleDateString();
			var week_end = (new Date(today.setDate(today.getDate() - today.getDay() + 6))).toLocaleDateString();
			if (lead_val == "this_week") {
				domain.push(['create_date', '>=', week_start], ['create_date', '<=', week_end], ['date_deadline', '=', false]);
			}
			this.do_action({
				type: 'ir.actions.act_window',
				name: 'Lead',
				res_model: 'crm.lead',
				views: [
					[false, 'tree'],
					[false, 'form']
				],
				domain: domain,
				context: context,
				target: 'current',
			});

		},

		onClick_this_year() {
			this.$('#lead_templates').empty();
			this.$('#opportunity_templates').empty();
			this.$('#expected_revenue').empty();
			this.$('#revenue').empty();
			this.$('#win_ratio').empty();
			var self = this
			var lead_val = this.$('#filter_values').val()
			rpc.query({
					model: 'crm.lead',
					method: 'get_year',
					args: [lead_val],
				})
				.then(function(data) {
					$('#lead_templates').append('<span>' + data.lead_templates + '</span>');
					$('#opportunity_templates').append('<span>' + data.opportunity_templates + '</span>');
					$('#expected_revenue').append('<span>' + data.currency_id + '</span>');
					$('#expected_revenue').append('<span>' + data.expected_revenue + '</span>');
					$('#revenue').append('<span>' + data.currency_id + '</span>');
					$('#revenue').append('<span>' + data.order_id + '</span>');
					$('#win_ratio').append('<span>' + data.win_ratio + '</span>');
				})
		},
		render_my_leads_graph: function() {
			var self = this;
			var ctx = self.$("#lead_chart");
			var ctx1 = self.$("#opr_chart");
			var ctx2 = self.$("#exp_revenue_chart");
			var ctx3 = self.$("#revenue_chart");
			rpc.query({
					model: 'crm.lead',
					method: 'get_lead_chart',
					args: [],
				})
				.then(function(results) {
					var lead_templates = results.lead_templates;
					var chart = new Chart(ctx, {
						type: "doughnut",
						data: {
							labels: Object.keys(lead_templates),
							datasets: [{

								backgroundColor: [
									'rgb(54, 162, 235)',
									'rgb(75, 192, 192)',
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(lead_templates),
								label: "Leads",
							}]
						},
					});
					var opportunity = results.opportunity;
					var chart1 = new Chart(ctx1, {
						type: "pie",
						data: {
							labels: Object.keys(opportunity),
							datasets: [{

								backgroundColor: [
									'rgb(255, 205, 86)',
									'rgb(255, 99, 132)',
									'rgb(54, 162, 235)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(opportunity),
								label: "Opportunities",
							}]
						},
					});
					var expected_revenue = results.expected_revenue;
					var chart2 = new Chart(ctx2, {
						type: "bar",
						data: {
							labels: Object.keys(expected_revenue),

							datasets: [{

								backgroundColor: [
									'rgba(255, 99, 132, 0.2)',
									'rgba(255, 159, 64, 0.2)',
									'rgba(255, 205, 86, 0.2)',
									'rgba(75, 192, 192, 0.2)',
									'rgba(54, 162, 235, 0.2)',
									'rgba(153, 102, 255, 0.2)',
									'rgba(201, 203, 207, 0.2)',
								],
								borderColor: [
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
									'rgb(75, 192, 192)',
									'rgb(54, 162, 235)',
									'rgb(153, 102, 255)',
									'rgb(201, 203, 207)',
								],
								data: Object.values(expected_revenue),
								label: "Amount",
								borderWidth: 1,
							}]
						},
						options: {
							scales: {
								y: {
									beginAtZero: true
								},
							},
							responsive: false,
							maintainAspectRatio: false,
						},
					});
					var chart3 = new Chart(ctx3, {
						type: "line",
						data: {
							labels: Object.keys(lead_templates),

							datasets: [{
								data: Object.values(lead_templates),
								label: "Count",
								fill: false,
								borderColor: 'rgb(75, 192, 192)',
								tension: 0.1,
							}]
						},
						options: {
							responsive: false,
							maintainAspectRatio: false,

						},
					});

				});
		},
		render_my_leads_graph_month: function() {
			this.$("#lead_chart").hide();
			this.$("#lead_chart_week").hide();
			this.$("#lead_chart_year").hide();
			this.$("#lead_chart_quarter").hide();
			this.$("#lead_chart_month").show();
			var self = this;
			var lead_val = this.$('#filter_values').val()

			var ctx = self.$("#lead_chart_month");

			rpc.query({
					model: 'crm.lead',
					method: 'get_lead_chart_values',
					args: [lead_val],
			    })
				.then(function(results) {
					var lead_templates = results.lead_templates;
					var chart = new Chart(ctx, {
						type: "doughnut",
						data: {
							labels: Object.keys(lead_templates),
							datasets: [{

								backgroundColor: [
									'rgb(54, 162, 235)',
									'rgb(75, 192, 192)',
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(lead_templates),
							}]
						},
					});
				});
		},


		render_my_leads_graph_year: function() {
			this.$("#lead_chart").hide();
			this.$("#lead_chart_week").hide();
			this.$("#lead_chart_quarter").hide();
			this.$("#lead_chart_month").hide();
			this.$("#lead_chart_year").show();
			this.$("#lead_chart_year").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			var ctx1 = self.$("#lead_chart_year");
			rpc.query({
					model: 'crm.lead',
					method: 'get_lead_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var lead_templates = results.lead_templates;
					var chart = new Chart(ctx1, {
						type: "doughnut",
						data: {
							labels: Object.keys(lead_templates),
							datasets: [{

								backgroundColor: [
									'rgb(54, 162, 235)',
									'rgb(75, 192, 192)',
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(lead_templates),
							}]
						},
					});
				});
		},
		render_my_leads_graph_week: function() {
			this.$("#lead_chart").hide();
			this.$("#lead_chart_quarter").hide();
			this.$("#lead_chart_year").hide();
			this.$("#lead_chart_month").hide();
			this.$("#lead_chart_week").show();
			this.$("#lead_chart_week").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			var ctx = self.$("#lead_chart_week");
			rpc.query({
					model: 'crm.lead',
					method: 'get_lead_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var lead_templates = results.lead_templates;
					var chart = new Chart(ctx, {
						type: "doughnut",
						data: {
							labels: Object.keys(lead_templates),
							datasets: [{

								backgroundColor: [
									'rgb(54, 162, 235)',
									'rgb(75, 192, 192)',
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(lead_templates),
							}]
						},
					});
				});
		},
		render_my_leads_graph_quarter: function() {
			this.$("#lead_chart").hide();
			this.$("#lead_chart_week").hide();
			this.$("#lead_chart_year").hide();
			this.$("#lead_chart_month").hide();
			this.$("#lead_chart_quarter").show();
			this.$("#lead_chart_quarter").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			var ctx = self.$("#lead_chart_quarter");
			rpc.query({
					model: 'crm.lead',
					method: 'get_lead_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var lead_templates = results.lead_templates;
					var chart = new Chart(ctx, {
						type: "doughnut",
						data: {
							labels: Object.keys(lead_templates),
							datasets: [{

								backgroundColor: [
									'rgb(54, 162, 235)',
									'rgb(75, 192, 192)',
									'rgb(255, 99, 132)',
									'rgb(255, 159, 64)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(lead_templates),
							}]
						},
					});
				});
		},

		render_opportunity_graph_month: function() {
			this.$("#opr_chart").hide();
			this.$("#opr_chart_week").hide();
			this.$("#opr_chart_year").hide();
			this.$("#opr_chart_quarter").hide();
			this.$("#opr_chart_month").show();
			this.$("#opr_chart_month").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			rpc.query({
					model: 'crm.lead',
					method: 'get_opportunity_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var ctx = self.$("#opr_chart_month");

					var opportunity = results.opportunity;
					var chart1 = new Chart(ctx, {
						type: "pie",
						data: {
							labels: Object.keys(opportunity),
							datasets: [{

								backgroundColor: [
									'rgb(255, 205, 86)',
									'rgb(255, 99, 132)',
									'rgb(54, 162, 235)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(opportunity),
								label: "Opportunities",
							}]
						},
					});
				});
		},

		render_opportunity_graph_quarter: function() {
			this.$("#opr_chart").hide();
			this.$("#opr_chart_week").hide();
			this.$("#opr_chart_year").hide();
			this.$("#opr_chart_month").hide();
			this.$("#opr_chart_quarter").show();
			this.$("#opr_chart_quarter").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			rpc.query({
					model: 'crm.lead',
					method: 'get_opportunity_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var ctx = self.$("#opr_chart_quarter");

					var opportunity = results.opportunity;
					var chart1 = new Chart(ctx, {
						type: "pie",
						data: {
							labels: Object.keys(opportunity),
							datasets: [{

								backgroundColor: [
									'rgb(255, 205, 86)',
									'rgb(255, 99, 132)',
									'rgb(54, 162, 235)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(opportunity),
								label: "Opportunities",
							}]
						},
					});
				});
		},

		render_opportunity_graph_year: function() {
			this.$("#opr_chart").hide();
			this.$("#opr_chart_week").hide();
			this.$("#opr_chart_quarter").hide();
			this.$("#opr_chart_month").hide();
			this.$("#opr_chart_year").show();
			this.$("#opr_chart_year").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			var ctx1 = self.$("#lead_chart_year");
			rpc.query({
					model: 'crm.lead',
					method: 'get_opportunity_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var ctx = self.$("#opr_chart_year");

					var opportunity = results.opportunity;
					var chart1 = new Chart(ctx, {
						type: "pie",
						data: {
							labels: Object.keys(opportunity),
							datasets: [{

								backgroundColor: [
									'rgb(255, 205, 86)',
									'rgb(255, 99, 132)',
									'rgb(54, 162, 235)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(opportunity),
								label: "Opportunities",
							}]
						},
					});
				});
		},

		render_opportunity_graph_week: function() {
			this.$("#opr_chart").hide();
			this.$("#opr_chart_quarter").hide();
			this.$("#opr_chart_year").hide();
			this.$("#opr_chart_month").hide();
			this.$("#opr_chart_week").show();
			this.$("#opr_chart_week").empty();
			var self = this;
			var lead_val = this.$('#filter_values').val()
			var ctx = self.$("#opr_chart_week");
			rpc.query({
					model: 'crm.lead',
					method: 'get_opportunity_chart_values',
					args: [lead_val],
				})
				.then(function(results) {
					var opportunity = results.opportunity;
					var chart1 = new Chart(ctx, {
						type: "pie",
						data: {
							labels: Object.keys(opportunity),
							datasets: [{

								backgroundColor: [
									'rgb(255, 205, 86)',
									'rgb(255, 99, 132)',
									'rgb(54, 162, 235)',
									'rgb(255, 205, 86)',
								],
								data: Object.values(opportunity),
								label: "Opportunities",
							}]
						},
					});
				});
		},

	});
	core.action_registry.add('crm_dashboard_tags', DashBoard);
	return DashBoard;
});