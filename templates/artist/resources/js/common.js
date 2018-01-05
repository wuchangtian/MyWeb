$(function() {
	new Clipboard('.btn-copy').on('success', function(e) {
		$(e.trigger).text('已复制');
	});
	$.ajaxSetup({
		timeout : 3000,
		error : function(xhr, status, e) {
			console.log(xhr, status, e);
			// toastr.error("请求出错了!");
		}
	});
	// 关注
	window.onFollowClick = function() {
		if (!checkLogin())
			return;
		var $this = $(this);
		var en = $this.data('follow');
		$.ajax({
			url : path + '/accounts/' + $this.data('id') + '/follow',
			type : en == '0' ? 'post' : 'delete'
		}).then(function(ret) {
			if (ret == 1) {
				if (en == '0') {
					$this.data('follow', '1');
					if ($this.data('fan') == '1')
						$this.html('<i class="fa fa-exchange"></i>&nbsp;互相关注');
					else
						$this.html('<i class="fa fa-check-square"></i>&nbsp;已关注');
				} else {
					$this.data('follow', '0');
					$this.text('关注');
				}
			}
		});
	};
	// 私信
	window.onGetChat = function() {
		if (!checkLogin())
			return;
		var $this = $(this);
		window.open(path + '/messages/chat/' + $this.data('id'));
	};

	// QQ
	window.onOpenQQ = function() {
		if (!checkLogin())
			return;
		var qq = $(this).data('qq');
		if (qq) {
			$('#qqModalNickname').text($(this).data('nickname'));
			$('#qqModalNumber').text(qq).attr('href', 'http://wpa.qq.com/msgrd?v=3&uin=' + qq + '&site=qq&menu=yes');
			$('#qqModal .btn-copy').attr('data-clipboard-text', qq).text('复制');
			$('#qqModal').modal();
		}
	};
	// 关注按钮
	$(document.body).on('click', '.btn-follow', onFollowClick);
	// 私信按钮
	$(document.body).on('click', '.btn-get-chat', onGetChat);
	// QQ按钮
	$(document.body).on('click', '.open-qq', onOpenQQ);

	// 赞事件
	$(document.body).on('click', '.work-zan', function() {
		if (!checkLogin())
			return;
		var $this = $(this);
		var en = $(this).hasClass('active');
		var domain = $this.data('domain') || 'works';
		$.ajax({
			url : path + '/' + domain + '/' + $this.data('id') + '/zan',
			type : !en ? 'post' : 'delete'
		}).then(function(ret) {
			if (ret == 1) {
				var countSpan = $this.find('.zan-count');
				var count = parseInt(countSpan.text());
				$this.toggleClass('active');
				count = en ? count - 1 : count + 1;
				countSpan.text(count);
			}
		});
	});

	var HISTORY_CONTACT_KEY = 'historyContacts';
	// 添加最近联系人
	window.addHistoryContact = function(id, nick, img) {

		var c = {
			id : id,
			nick : nick,
			img : img
		};
		// 获取联系人列表
		var list = getHistoryContacts();
		if (!list)
			list = [];
		for (var i = 0; i < list.length; i++) {
			if (list[i].id == id) {
				// 移除要添加联系人
				list.splice(i, 1);
				break;
			}
		}
		list.push(c);
		$.cookie(HISTORY_CONTACT_KEY, list, {
			path : '/'
		});
	}

	// 删除一个最近联系人
	window.removeHistoryContact = function(id) {

		// 获取联系人列表
		var list = getHistoryContacts();
		if (list)
			for (var i = 0; i < list.length; i++) {
				if (list[i].id == id) {
					// 移除联系人
					list.splice(i, 1);
					$.cookie(HISTORY_CONTACT_KEY, list, {
						path : '/'
					});
					break;
				}
			}
	}

	// 获取最近联系人列表
	window.getHistoryContacts = function() {
		return $.cookie(HISTORY_CONTACT_KEY);
	}

	// 删除联系人列表
	window.removeHistoryContacts = function() {
		$.removeCookie(HISTORY_CONTACT_KEY, {
			path : '/'
		});
	}

	// 检查登录
	window.checkLogin = function() {
		if ($('#visitor').val() == 1) {
			$('#loginModal').modal();
			return false;
		}
		return true;
	}

	// 返回顶部
	window.scrollTop = function() {
		$(document.body).scrollTop(0);
	};

	window.innerSearch = function(domain, text, params) {
		text = encodeURI($.trim(text));
		var params0 = {
			q : text
		};
		if (params) {
			$.extend(params0, params);
		}
		window.open(path + '/search/' + domain + '?' + $.param(params0), '_self')
	}

	// 页头搜索
	window.globalSearch = function() {
		innerSearch('work', $('#searchInput').val())
	}

	// 页头搜索
	$('#searchInput').keypress(function(e) {
		if (e.keyCode == 13)
			globalSearch();
	});
	$('#btnSearch').click(globalSearch);

	$('#navCollectLink').click(function() {
		$.ajax({
			url : path + '/collect/hasRight?t=' + new Date().getTime()
		}).then(function(right) {
			if (right == 1) {
				window.location.href = path + '/collects/newCollect';
			} else {
				$('#navCollectRightModal').modal('show');
			}
		}, function() {
		});
	});

	window.checkUnonload = function() {
		window.needunload = true;
		window.onbeforeunload = function() {
			if (window.needunload)
				return '内容尚未保存，你确定要离开么？';
		};
	};

});