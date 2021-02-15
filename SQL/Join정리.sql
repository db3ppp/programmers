#Equi Join
#두 table에서 공통적으로 존재하는 컬럼 값이 일치되는 행 연결
select e.ename, d.dname from emp e, dept d
where e.deptno = d.deptno
and e.JOB = 'MANAGER';

#Non-Equi Join
#where절에서 '='연산자 이외의 비교 연산자 사용하는 경우
select e.ename,e.sal, s.grade from emp e,salgrade s
where e.sal between s.losal and s.hisal;

#Self Join
#자기자신과 조인: 원하는 정보가 같은 table에 있을 경우
#scott과 동일한 근무지에서 근무하는 사원의 이름
select e1.ename, e2.ename from emp e1, emp e2
where e1.deptno=e2.deptno and e1.ename = 'SCOTT' and e2.ename <>'SCOTT';

#Outer Join
#무조건 main table의 튜플 갯수만큼 보장해준다
select employee.ename || '의 매니저는'
    ||manager.ename ||'입니다'
from emp employee, emp manager
where employee.mgr = manager.empno(+);

