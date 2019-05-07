% rebase('layout.tpl', title='RUT Page')

<div class="jumbotron">
<form action="/rut" method="post">
            RUT: <input name="rut" type="text" />
            <input value="Validar" type="submit" />
        </form>
		{{ rut_str }}
</div>