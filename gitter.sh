# Script for making a few GIT commands in an easy way
# dvg

print_intro() {
	echo GIT Script Executor
	echo "----------------------------------------------------"
	echo "GIT utility script by Danny Van Geyte"
	echo "----------------------------------------------------"
}

usage() {
	echo "./gitters.sh [option]"
	echo "   where option = s   : show status"
	echo "                  c   : commit"
	echo "                  p   : push"
	echo "                  a   : add files only"
	echo "                  all : full stack operation"
}

add_files() {
	git add *
}

show_stat() {
	git status
}

commit_now() {
	git add *
	read -p "Commit description: " mesg
	git commit -m "$mesg"

}

do_push() {
	git add *
	read -p "Commit description: " mesg
	git commit -m "$mesg"
	git push -u origin master
}

print_intro

case $1 in 
	a)
		show_stat
		add_files
		;;
	s)
		show_stat
		;;
	c)
		commit_now
		;;
	p)
		do_push
		;;
	all)
		show_stat
		do_push
		;;
	*)
		usage
		;;
esac
	